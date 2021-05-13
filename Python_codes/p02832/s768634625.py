N=int(input())
a=list(map(int,input().split()))
i=1
f=False
for ai in a:
    if ai==i:
        i+=1
        f=True

if f:
    print(N-i+1)
else:
    print(-1)