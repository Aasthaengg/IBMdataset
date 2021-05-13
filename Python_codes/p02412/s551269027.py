while(True):
    n, x = map(int, input().split())
    if(n == x == 0): break
    ans = 0
    for x1 in range(1, n-1):
        for x2 in range(x1+1, n):
            for x3 in range(x2+1, n+1):
                if((x1 + x2 + x3) == x):
                    ans += 1
    print(ans)