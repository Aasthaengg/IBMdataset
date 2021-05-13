N,C,K=map(int,input().split())
T=sorted([int(input()) for i in range(N)])
lt=T[0]+K
m=0
b=0
for t in T:
    if lt>=t and m<C:
        m+=1
    else:
        m=1
        b+=1
        lt=t+K
if m>=1:
    b+=1
print(b)
