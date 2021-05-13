n=int(input())

v=list(map(int,input().split()))
c=list(map(int,input().split()))

x=0
for i in range(2**n):
    cost=0
    value=0
    for j in range(n):
        if i>>j&1:
            cost+=c[j]
            value+=v[j]
    else:
        if value-cost>x:
            x=value-cost
            


print(x)
         
