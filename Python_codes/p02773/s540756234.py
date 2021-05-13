from collections import defaultdict

n = int(input())
counter = defaultdict(int)
for _ in range(n):
    s = input()
    counter[s] += 1

l = [(-n, s) for s, n in counter.items()]
l.sort()
m = l[0][0]

for x, s in l:
    if x != m:
        break
    print(s)
