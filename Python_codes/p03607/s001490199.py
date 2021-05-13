import collections


def solve():
    pass


n = int(input())
A = []
for i in range(n):
    a = int(input())
    A.append(a)

c = collections.Counter(A)
cnt = 0
for k, v in c.items():
    if v % 2 == 0: continue
    else: cnt += 1
print(cnt)