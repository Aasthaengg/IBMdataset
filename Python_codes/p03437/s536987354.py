X,Y = map(int,input().split())
if X%Y == 0:
    print(-1)
else:
    ans = X
    while ans <= 10**18:
        if ans % Y != 0:
            break
        ans += ans
    if ans > 10**18:
        print(-1)
    else:
        print(ans)
