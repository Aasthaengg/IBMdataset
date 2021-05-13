N,A,B,C=map(int,input().split())
L=[]
for i in range(0,N):
    L.append(int(input()))

ans=float('inf')
for i in range(0,4**N):
    a=0
    b=0
    c=0
    MP=0
    for j in range(0,16):
        if i>>(2*j) & 1==1 and i>>(2*j+1) &1==0:
            a+=L[j]
            MP+=10
        elif i>>(2*j) & 1==0 and i>>(2*j+1) &1==1:
            b+=L[j]
            MP+=10
        elif i>>(2*j) & 1==1 and i>>(2*j+1) &1==1:
            c+=L[j]
            MP+=10

    if a*b*c==0:
        continue
    else:
        MP-=30
        MP+=abs(a-A)+abs(b-B)+abs(c-C)
        ans=min(MP,ans)

print(ans)