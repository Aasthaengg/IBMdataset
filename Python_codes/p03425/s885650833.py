from collections import Counter
import itertools

N = int(input())
S = [input()[0] for _ in range(N)]
counter = Counter(S)

ans = 0
for x,y,z in itertools.combinations('MARCH',3):
    ans += counter[x] * counter[y] * counter[z]

print(ans)
