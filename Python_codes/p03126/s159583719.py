N,M=map(int,(input().split()))
k=list(map(int,input().split()))[1:]
for i in range(N-1):
  A=list(map(int,input().split()))[1:]
  l=[]
  for j in k:
    if j in A:
      l.append(j)
  k=l
print(len(k))
