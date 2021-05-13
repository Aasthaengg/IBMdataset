from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
mod = 10**9 + 7
cnt = defaultdict(int)

for i in a:
    cnt[i] += 1

ans = 1
if n % 2 == 0:
    for _ in range(n // 2):
        ans *= 2
        ans %= mod
    if cnt[0] == 0:
        check = [2 * i + 1 for i in range(n // 2)]
        for i in check:
            if cnt[i] != 2:
                ans = 0
                break
    else:
        ans = 0

else:
    for _ in range((n-1)//2):
        ans *= 2
        ans %= mod
    if cnt[0] == 1:
        check = [2 * i + 2 for i in range((n-1)//2)]
        for i in check:
            if cnt[i] != 2:
                ans = 0
                break

    else:
        ans = 0

print(ans)

