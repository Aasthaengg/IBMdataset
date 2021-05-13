n,k=map(int,input().split())
t,*s=input()
c=0
for d in s:
  if d==t: c+=1
  t=d
print(min(c+k*2,n-1))