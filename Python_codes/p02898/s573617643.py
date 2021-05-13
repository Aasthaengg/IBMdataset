a,b=map(int,input().split())
c=0
l=list(map(int,input().split()))
for i in range(len(l)):
  if l[i]>=b:
    c+=1 
print(c)