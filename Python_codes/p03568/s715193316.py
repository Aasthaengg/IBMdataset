import itertools


n = int(input())
a = list(map(int, input().split()))

ans = 0
for ptn in itertools.product(range(-1, 2), repeat=n):
    for i, num in enumerate(ptn):
        if (a[i] + num) % 2 == 0:
            ans += 1
            break
print(ans)