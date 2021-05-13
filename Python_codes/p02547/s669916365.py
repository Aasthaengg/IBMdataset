n=int(input())
j=0
r="No"
for i in range(n):
  l,m=map(int,input().split())
  if(l==m):
    j+=1
  else:
    j=0
  if(j==3):
    r="Yes"
    break
print(r)
    
