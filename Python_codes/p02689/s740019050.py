n,m=map(int,input().split())
H=list(map(int,input().split()))
x=[1]*n
for i in range(m):
    a,b=map(int,input().split())
    if H[a-1]>H[b-1]:
        x[b-1]=0
    elif H[a-1]==H[b-1]:
        x[a-1]=0
        x[b-1]=0
    else:
        x[a-1]=0

print(sum(x))