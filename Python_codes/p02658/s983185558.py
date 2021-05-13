n = int(input())
a = list(map(int, input().split()))

res = 1
if 0 in a:
    print(0)
else:
    for i in range(n):
        res *= a[i]
        if res > 10**18:
            res = -1
            break
    print(res)