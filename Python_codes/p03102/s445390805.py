n,m,c=input().split(" ")
cnt=0
n,m,c=int(n),int(m),int(c)
lst=[]
for i in range(n+1):
  lst.append(input().split(" "))

for i in range(1,n+1):
  ans=c
  for j in range(m):
    ans+=int(lst[i][j])*int(lst[0][j])
  if ans>0:
    cnt+=1
print(cnt)