a,b,c = map(int,input().split())
ans = 0
p = 0

for i in range(c):
    if int(a/2)*2==a and int(b/2)*2==b and int(c/2)*2==c:
        if a == b and b == c:
            break
        ans += 1
        x = b / 2 + c / 2
        y = a / 2 + c / 2
        z = b / 2 + a / 2
        a = x
        b = y
        c = z

    else:
        p = 1
        print(ans)
        break



if p == 0:
    print(-1)