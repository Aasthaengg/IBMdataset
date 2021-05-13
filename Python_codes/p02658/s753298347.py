n = int(input())
a = sorted(list(map(int, input().split())))

m = 10**18
if a[0] == 0:
    print(0)
else:
    ans = 1
    for i in a:
        ans *= i
        if ans > m:
            print(-1)
            exit()
    print(ans)