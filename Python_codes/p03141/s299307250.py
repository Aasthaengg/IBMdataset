N=int(input())
L=[]
for i in range(N):
    a,b=map(int, input().split())
    L.append((a,b,a+b))

L=sorted(L, reverse=True, key=lambda x: x[2])
taka=0
ao=0
for i in range(N):
    l=L[i]
    a,b,_=l
    if i%2==0:
        taka+=a
    else:
        ao+=b
print(taka-ao)