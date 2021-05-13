from collections import Counter
# 3 2
# 4 1 5
# N, M = map(int, '3 2'.split())
# As = list(map(int, '4 1 5'.split()))
N, M = map(int, input().split())
As = list(map(int, input().split()))

ct = Counter()
ct[0] = 1

ans = 0
s = 0
for a in As:
	s+=a
	ans += ct[s%M]
	ct[s%M] += 1

print(ans)

