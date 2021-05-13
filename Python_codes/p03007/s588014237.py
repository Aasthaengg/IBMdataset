n=int(input())
L=list(map(int,input().split()))
L.sort()
ans=[]
for i in range(1,n-1):
  if L[i]>0:
    ans.append((L[0],L[i]))
    L[0]-=L[i]
for i in range(n):
  if L[i]>0 or len(ans) == n-1:
    break
  else:
    ans.append((L[n-1],L[i]))
    L[n-1]-=L[i]
print(L[n-1])
for a in ans:
  x,y=a
  print(x,y)
