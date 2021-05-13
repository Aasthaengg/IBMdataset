from itertools import combinations_with_replacement as comb_rplc
n, m, q = list(map(int, input().split()))
req = [list(map(int, input().split())) for _ in range(q)]

ans = 0

for seq in comb_rplc(range(1,m+1),n):
    now = 0
    for a, b, c, d in req:
        if seq[b-1] - seq[a-1] == c:
            now += d
    ans = max(ans, now)

print(ans)