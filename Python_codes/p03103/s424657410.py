n,m=map(int,input().split())
a=[]
for _ in range(n):
    A=list(map(int,input().split()))
    a.append(A)
a.sort()
ans=0
for i in a:
    if m>i[1]:
        ans+=i[0]*i[1]
        m-=i[1]
    else:
        ans+=m*i[0]
        print(ans)
        exit()
