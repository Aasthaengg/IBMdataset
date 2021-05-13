N, C = map(int, input().split())
sushi = [(0, 0)]
for _ in range(N):
    x, v = map(int, input().split())
    sushi.append((x, v))
# preprocess
cumsum = [(0, 0)]
cumsum_max = [(0, 0)]
prev = 0
for x, v in sushi[1:]:
    cumsum.append((x, cumsum[-1][1] + prev + v - x))
    cumsum_max.append(cumsum_max[-1] if cumsum_max[-1][1] > cumsum[-1][1] else cumsum[-1])
    prev = x
cumsum_rev = [(0, 0)]
cumsum_rev_max = [(0, 0)]
prev = 0
for x, v in reversed(sushi[1:]):
    cumsum_rev.append((C - x, cumsum_rev[-1][1] + prev + v - (C - x)))
    cumsum_rev_max.append(cumsum_rev_max[-1] if cumsum_rev_max[-1][1] > cumsum_rev[-1][1] else cumsum_rev[-1])
    prev = C - x
ans = 0
for i in range(N+1):
    temp1 = cumsum_max[N-i][1] + cumsum_rev[i][1] - cumsum_rev[i][0]
    temp2 = cumsum_rev_max[N-i][1] + cumsum[i][1] - cumsum[i][0]
    ans = max(ans, temp1, temp2)
print(ans)