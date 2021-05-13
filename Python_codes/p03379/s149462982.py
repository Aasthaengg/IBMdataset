n=int(input())
x=list(map(int,input().split()))
y=sorted(x)
L=y[n//2-1]
R=y[n//2]
for i in range(n):
    if x[i]<=L:
        print(R)
    else:
        print(L)