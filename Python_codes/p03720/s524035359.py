N,M = map(int,input().split())
A = [0]*N

for m in range(M):
  a,b = map(int,input().split())
  A[a-1]+=1
  A[b-1]+=1
print(*A,sep="\n")