N,K,Q = map(int,input().split())
res = [K-Q]*N

for _ in range(Q):
  A = int(input())-1
  res[A] += 1
  
for i in range(N):
  if res[i]>0:
    print("Yes")
  else:
    print("No")