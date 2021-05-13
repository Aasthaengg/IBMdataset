## code borrowed from "maspy"

import numpy as np
import sys
buf = sys.stdin.buffer
 
H,W = map(int,buf.readline().split())
# 周りに壁を、0,1化、壁を0で持つ
grid = np.zeros((H+2,W+2),dtype=np.bool)
grid[1:-1,1:] = (np.frombuffer(buf.read(H*(W+1)),dtype='S1') == b'.').reshape((H,W+1))
 
# x軸方向の集計
def F(transpose):
  x = grid
  if transpose:
    x = (x.T).copy()
  x = np.ravel(x) # to 1D array
  L = len(x)
  
  left_zero = np.where(x,0,-np.arange(L)) # 左の壁のindexの-1倍
  np.minimum.accumulate(left_zero, out=left_zero)
  
  right_zero = np.where(x[::-1],0,np.arange(L)) # 逆順ソートした上で左の壁のindex
  np.maximum.accumulate(right_zero, out=right_zero)
  
  y = left_zero
  y += L-right_zero[::-1]
  
  return y.reshape(grid.T.shape).T if transpose else y.reshape(grid.shape)
  
answer = (F(False) + F(True)).max()-5
print(answer)