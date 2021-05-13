N=int(input())
ab=[list(map(int,input().split()))for _ in range(N)]
ans=0
for a,b in ab[::-1]:
    a+=ans
    if a%b==0:
        ans+=0
    else:
        ans+=b-a%b
print(ans)