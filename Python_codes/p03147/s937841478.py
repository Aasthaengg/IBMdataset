N=int(input())
h=list(map(int,input().split()))
l=[0]*N
z=0
for i in range(0,100):
    f=False
    for j in range(0,N):
        if h[j]>i:
            if not f:
                f=True
        else:
            if f:
                f=False
                z+=1
    if f:
        z+=1

print(z)