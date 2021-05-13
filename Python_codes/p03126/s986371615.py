N,M = map(int,input().split())
L = [0]*31

for n in range(N):
  K,*A = map(int,input().split())
  for a in A:
    L[a]+=1
    
print(L.count(N))