from itertools import groupby
n = int(input())
P = list(map(int, input().split()))

j = [False] * (n+1)
for i, p in enumerate(P):
    if i+1 == p:
        j[i] = True

cnt = 0
gr = groupby(j)
for key, group in gr:
    l = len(list(group))
    if key and l != 1:
        cnt += l//2 if l % 2 == 0 else l//2+1
    elif key:
        cnt += 1

print(cnt)