n = int(input())
a = list(map(int, input().split()))
fac = [1 for _ in range(n+1)]
mod = 10 ** 9 + 7

ans = 1

cnt = [0, 0, 0]
for i in range(n):
    ans = ans * cnt.count(a[i]) % mod
    for j in range(3):
        if a[i] == cnt[j]:
            cnt[j] += 1
            break

print(ans)