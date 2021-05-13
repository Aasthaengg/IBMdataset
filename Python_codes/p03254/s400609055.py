n, x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
ans = [0]*n
if (sum(a) == x):
    print(n)
else:
    for i in range(n):
        if (x >= a[i]):
            ans[i] = 1
            x -= a[i]
        else:
            print(sum(ans))
            exit()
    if (0 in ans):
        print(sum(ans))
    else:
        print(sum(ans)-1)