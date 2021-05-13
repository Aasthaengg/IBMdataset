# 現在の数curに対して直前の数としてあり得る範囲は、cur ~ cur + A[i] - 1の範囲内
# さらにA[i-1]の倍数である必要があるため、上記範囲内のA[i-1]の倍数の最大最小値を設定する
# 直前の数がない場合(最後)はcur, cur + A[i]をそのまま出力
import sys
readline = sys.stdin.readline

K = int(readline())
A = list(map(int,readline().split()))[::-1] # ややこしいので逆順で見ていく

mincur = 2
maxcur = 2

def get_min_val(c,a): # c以上のaの倍数の最小値を求める
  return ((c - 1)//a + 1) * a

def get_max_val(c,a): # c以下のaの倍数の最大値を求める
  return (c // a) * a

if A[0] != 2:
  print(-1)
  exit(0)
  
for i in range(len(A)):
  mincur = mincur
  maxcur = maxcur + A[i] - 1
  if i + 1 < len(A):
    mincur = get_min_val(mincur,A[i + 1])
    maxcur = get_max_val(maxcur,A[i + 1])
    if mincur > maxcur:
      print(-1)
      exit(0)
print(mincur,maxcur)
