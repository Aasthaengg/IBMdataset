import collections
N = int(input())
S = [sorted(input()) for i in range(N)]
SS = []
for i in S:
    SS.append("".join(i))
count = 0

c = collections.Counter(SS)

for i in c.values():
    count += (i*(i-1)) // 2

print(count)