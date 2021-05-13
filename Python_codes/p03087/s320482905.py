n,q=list(map(int,input().split()))
s=input()

acum=[0]*(n+1)

for i in range(1,n):
    if s[i]=='C' and s[i-1]=='A':
        acum[i]=acum[i-1]+1
    else:
        acum[i]=acum[i-1]

for _ in range(q):
    l,r=list(map(int,input().split()))
    l-=1
    r-=1
    print(acum[r]-acum[l])