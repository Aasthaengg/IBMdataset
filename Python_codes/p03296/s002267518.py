from itertools import groupby

N = int(input())
A = list(map(int, input().split()))

A = groupby(A)
cnt = 0
for _, a in A:
    cnt += len(list(a)) // 2

print(cnt)