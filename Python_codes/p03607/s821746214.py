from collections import defaultdict
p = defaultdict(int)
for q in range(int(input())):
    a = int(input())
    p[a] += 1
ans = 0
for q in p.values():
    ans += 1 if q % 2 else 0
print(ans)