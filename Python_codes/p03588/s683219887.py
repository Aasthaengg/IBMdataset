N=int(input())
maxrank=10**5+1
minrank=0
minpoint=10**9+1
for i in range(N):
  a,b=map(int,input().split())
  maxrank=min(maxrank,a)
  minrank=max(minrank,a)
  minpoint=min(minpoint,b)
print((minrank-maxrank+1)+(maxrank-1)+minpoint)