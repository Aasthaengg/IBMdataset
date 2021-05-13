n=int(input())
a=list(map(int,input().split()))
x=[]
ans=1

for i in range(n-1):
  if a[i+1]==a[i]:
    continue
  x.append(a[i+1]-a[i])
  
flag=True

for i in range(len(x)-1):
  if flag==False:
    flag=True
    continue
  if x[i]<0 and x[i+1]>0 or x[i]>0 and x[i+1]<0:
    ans+=1
    flag=False
    

print(ans)
