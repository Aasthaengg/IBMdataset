n,m=map(int,input().split())
L=2**n
cost=[0]+[10**8 for i in range(L-1)]

for i in range(m):
    a,b=map(int,input().split())
    c=sum([2**(int(i)-1) for i in input().split()])
    for j in range(L):
        q=j|c
        x=cost[j]+a
        if cost[q]>x:
            cost[q]=x
print(cost[L-1] if cost[L-1]<10**8 else -1)