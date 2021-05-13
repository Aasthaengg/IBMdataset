inf = 1 << 20
need = -1, 2, 5, 5, 4, 5, 6, 3, 7, 6

n, m = map(int, input().split())
a = map(int, input().split())
d = {need[x]: x for x in sorted(a)}  # sortedで昇順にすることで、同じ本数のとき最大値が残る
e = tuple(sorted(d.items(), key=lambda x: x[1], reverse=True))  # (必要本数,数字)

dp = [-inf] * (n + 1)
dp[0] = 0
# dp[k]:=k本で構成可能な最大桁数

for j in range(1, n + 1):
    dp[j] = max((dp[j - cnt] for cnt, _ in e if j - cnt >= 0), default=-inf) + 1

ret = []
r = dp[n]

curr = n
while r > 0:
    for cnt, num in e:
        if curr - cnt >= 0 and dp[curr - cnt] == r - 1:
            ret.append(num)
            r -= 1
            curr -= cnt
            break

ret.sort(reverse=True)
print(''.join(map(str, ret)))
