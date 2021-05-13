n,m=map(int,input().split())
seito=[]
for i in range(n):
    a,b=map(int,input().split())
    seito.append([a,b])
point=[]
for i in range(m):
    c,d=map(int,input().split())
    point.append([c,d])

ans=[float("inf")]*n
for i in range(n):
    a,b=seito[i]
    min_kyori=float("inf")
    for j in range(m):
        c,d=point[j]
        kyori=abs(a-c)+abs(b-d)
        if kyori<min_kyori:
            min_kyori=kyori
            ans[i]=j+1

for i in ans:
    print(i)