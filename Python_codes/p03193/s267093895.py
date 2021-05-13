n,h,w=map(int,input().split())
lst=[list(map(int,input().split())) for i in range(n)]
ans=0
for e in lst:
    ans+=(e[0]>=h and e[1]>=w)
print(ans)
