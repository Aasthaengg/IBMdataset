n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

if sum(a) < sum(b):
    print(-1)
else:
    x = sorted([a[i]-b[i] for i in range(n)], reverse=True)
    s = -sum(d for d in x if d < 0)
    ans = sum(1 for d in x if d < 0)
    i = 0
    while s > 0:
        s -= x[i]
        ans += 1
        i += 1
    print(ans)