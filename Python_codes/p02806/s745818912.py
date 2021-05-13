n=int(input())
arr=[]
for _ in range(n):
  s,t=map(str,input().split())
  arr.append([s,int(t)])
x=input()
ans=0
flag=False
for i in range(n):
  if flag==True:
    ans+=arr[i][1]
  if arr[i][0]==x:
    flag=True
print(ans)