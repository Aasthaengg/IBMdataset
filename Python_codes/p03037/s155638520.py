n, m = map(int, input().split())
cards = [0] * n
for i in range(m):
    l, r = map(lambda x: int(x)-1, input().split())
    cards[l] += 1
    if r+1 < n:
        cards[r+1] -= 1

from itertools import accumulate
ac = list(accumulate(cards))

ans = 0
for a in ac:
    if a == m:
        ans += 1
print(ans)
