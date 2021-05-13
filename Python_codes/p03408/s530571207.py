from collections import Counter
N = int(input())
s = Counter([input().strip() for i in range(N)])
M = int(input())
t = Counter([input().strip() for i in range(M)])
r = 0
for k, v in s.items():
    r = max(r, v-t.get(k, 0))
print(r)
