from collections import Counter
N = int(input())
s = [str(sorted(input())) for _ in range(N)]
c = Counter(s)

cnt = []
for i in c.values():
    cnt.append(i * (i - 1)//2)
print(sum(cnt))
