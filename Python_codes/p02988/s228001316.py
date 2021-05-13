n=int(input())
p=list(map(int,input().split()))
c=0
for i in range(1,n-1):
  if min(p[i-1],p[i+1])<p[i]<max(p[i-1],p[i+1]):
    c+=1
print(c)