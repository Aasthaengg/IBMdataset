a,b,c = map(int,input().split())

if a==b==c and a%2==0 and b%2==0 and c%2 == 0:
    print(-1)
else:
    ans = 0
    while True:
        if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
            break
        a,b,c = (b/2+c/2), (a/2+c/2), (a/2+b/2)
        ans += 1
    print(ans)