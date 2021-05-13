N,T = map(int,input().split())
X = [list(map(int,input().split())) for n in range(T)]
M = N
m = 0

for a,b in X:
  M = min(M,b)
  m = max(m,a)
  
if M<m:
  print(0)
else:
  print(M-m+1)