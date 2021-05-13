a,b,c = map(int,input().split())
if a % 2 == 0 and a == b == c:
    print(-1)
else:
    ans = 0
    while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        ab,bc,ac = a//2+b//2,b//2+c//2,a//2+c//2
        a,b,c = bc,ac,ab
        ans += 1
    print(ans)