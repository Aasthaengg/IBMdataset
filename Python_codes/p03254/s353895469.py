N,x=map(int,input().split())
a=list(map(int,input().split()))
result=0
a.sort()
for i in range(N):
  n=a.pop(0)
  if x>=n:
    x-=n
    result+=1
  else:
    break
else:
  if not x==0:
    result-=1
print(result)