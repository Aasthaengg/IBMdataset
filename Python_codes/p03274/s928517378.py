import sys
readline = sys.stdin.readline

N,K = map(int,readline().split())
X = list(map(int,readline().split()))

if 0 in X: # 座標0にろうそくがあるなら一本消せる
  K -= 1
  
plus = []
minus = []
for x in X:
  if x < 0:
    minus += [-x]
  elif x > 0:
    plus += [x]
    
minus = [0] + minus[::-1]
plus = [0] + plus

ans = 10 ** 10
for m in range(K + 1):
  p = K - m
  if m < len(minus) and p < len(plus):
    dist = min(minus[m],plus[p]) * 2 + max(minus[m],plus[p])
    if ans > dist:
      ans = dist
      
print(ans)
  
  

    
