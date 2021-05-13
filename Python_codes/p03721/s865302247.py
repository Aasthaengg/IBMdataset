n,k=map(int,input().split())

backet=[0]*(10**5+1)
for i in range(n):
    a,b=map(int,input().split())
    backet[a]+=b

for i in range(1,10**5+1):
    if backet[i] >= k:
        print(i)
        exit()
    k-=backet[i]
