N,M = map(int,input().split())
R = [set([]) for _ in range(N)]
for i in range(M):
  a,b = map(int,input().split())
  a-=1;b-=1
  R[a].add(b)
  R[b].add(a)
#print(R)
for i in range(1,N-1):
  if 0 in R[i] and N-1 in R[i]:
    print("POSSIBLE")
    exit()
print("IMPOSSIBLE")