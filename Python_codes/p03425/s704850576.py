import sys
import itertools

N = int(sys.stdin.readline())

count = {"M": 0, "A": 0, "R": 0, "C": 0, "H": 0}
for _ in range(N):
    s = sys.stdin.readline().strip()
    if s[0] in count:
        count[s[0]] += 1

ans = 0
for perm in itertools.combinations(count.keys(), 3):
    tmp = 1
    for i in perm:
        tmp *= count[i]
    ans += tmp

print(ans)