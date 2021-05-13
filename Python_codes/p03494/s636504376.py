n=int(input())
l=list(map(int,input().split()))
d=[]
for i in range(n):
    c=0
    x=l[i]
    while(x%2==0):
        c+=1
        x=x//2
    d.append(c)
m=min(d)
print(max(0,m))
