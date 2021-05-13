n,m=map(int,input().split())
I=list(map(int,input().split()))
for i in range(m):
    n-=I[i]
    if n<0:
        print("-1")
        exit()
print(n)

