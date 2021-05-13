n,m=map(int,input().split())
if n%2==1:
    x=""
    for i in range(m):
        x+=f"{i+1} {n-i} "
    print(x)
else:
    x=""
    for i in range(m):
        x+=(f"{i+1} {n-i} " if i<m/2 else f"{i+1} {n-i-1}\n")
    print(x)