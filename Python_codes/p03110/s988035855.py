N=int(input())
ans=0

for i in range(N):
    a=input().split()
    if a[1]=='JPY':
        ans+=int(a[0])
    else:
        ans+=float(a[0])*380000

print(ans)