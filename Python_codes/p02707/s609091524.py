import collections
N = int(input())
A = list(map(int, input().split()))

c = collections.Counter(A)
for i in range(1, N + 1):
    if i in c:
        print(c[i])
    else:
        print(0)
