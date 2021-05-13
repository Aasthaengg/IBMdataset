n,m=map(int,input().split())
L=[0]*n
for i in range(n):
    a,b=map(int,input().split())
    L[i]=[a,b]
L=sorted(L,key=lambda x:x[0])
cnt=m
ans=0
for i in L:
    if cnt<=i[1]:
        ans+=i[0]*cnt
        break
    ans+=i[1]*i[0]
    cnt-=i[1]
print(ans)