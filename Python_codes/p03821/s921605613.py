n=int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
ab=ab[::-1]
#print(ab)
ans=0
for a,b in ab:
    if (a+ans)%b!=0:
        ans+=b-(a+ans)%b
print(ans)