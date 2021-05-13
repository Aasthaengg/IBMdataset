import collections
N = int(input())
A = [input() for _ in range(N)]
c = collections.Counter(A)
cnt = 0
for i in set(A):
    if c[i]%2 == 1:
        cnt += 1
print(cnt)