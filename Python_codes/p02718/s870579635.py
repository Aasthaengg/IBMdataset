n,m=map(int,input().split())
l=list(map(int,input().split()))
s=sum(l)/(4*m)
c=0
for i in range(n):
    if(l[i]>=s):
        c=c+1
if(c>=m):
    print("Yes")
else:
    print("No")
