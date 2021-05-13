n=int(input())
v=list(map(int,input().split()))
c=list(map(int,input().split()))
m=0
for i in range(0,n):
    p=v[i]-c[i]
    if p>0:
        m+=p
    else:
        continue
print(m)