X, Y = list(map(int,input().split()))
if X == Y:  print(1)
else:
    ans = 0
    while X <= Y:
        X *= 2
        ans += 1
    print(ans)