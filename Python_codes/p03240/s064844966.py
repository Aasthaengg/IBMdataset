# 1つ見れば、マス目に対する高さが確定する
# 100件についてテスト
import numpy as np
N = int(input())
U = 100
XYH = np.array([[int(x) for x in input().split()] for _ in range(N)])
XYH = XYH[np.argsort(-XYH[:,2])] # 高い順なので0番目は正

x0,y0,h0 = XYH[0]
dx = np.abs(np.arange(U+1) - x0)
dy = np.abs(np.arange(U+1) - y0)
# そこに頂上があるとするとその高さ
H = dx[:,None] + dy[None,:] + h0
possible = np.full_like(H, True)

for x,y,h in XYH[1:]:
  dx = np.abs(np.arange(U+1) - x)
  dy = np.abs(np.arange(U+1) - y)
  possible &= (np.maximum(H-dx[:,None]-dy[None,:],0) == h)

nz = possible.nonzero()
x,y = nz[0][0], nz[1][0]
h = H[x,y]
print(x,y,h)
