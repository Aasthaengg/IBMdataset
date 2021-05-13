n,k=map(int,input().split())

if k>(n-1)*(n-2)//2:
    print(-1)
    exit()

ansl=[(1,i) for i in range(2,n+1)]
now=[]
for i in range(2,n+1):
    for j in range(i+1,n+1):
        now.append((i,j))

ansl+=now[:(n-1)*(n-2)//2-k]
print(len(ansl))
for i,j in ansl:
    print(i,j)
