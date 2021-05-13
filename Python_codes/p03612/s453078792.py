n=int(input())
p=list(map(int,input().split()))
c=0
for i in range(n-1):
 if p[i]==i+1:p[i],p[i+1]=p[i+1],p[i];c+=1
print(c+1 if p[n-1]==n else c)