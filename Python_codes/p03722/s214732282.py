n,m=map(int,input().split())
abc=[]
for i in range(m):
    abc.append([int(j) for j in input().split()])
b=[float("INF")]*(n+1)
b[1]=0
for i in range(1,n+1):
    for s,t,u in abc:
        if b[t]>b[s]-u:
            b[t]=b[s]-u
            if i==n and t==n:
                print("inf")
                exit()
print(-b[-1])