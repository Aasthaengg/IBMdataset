N,T = map(int,input().split())
P = list(map(int,input().split()))

total = T
now = T

for i in range(1,N):
  if now > P[i]:
    total += T - (now - P[i])
  else:
    total += T
  now = P[i] + T
    
print(total)