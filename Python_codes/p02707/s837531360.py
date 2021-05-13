N = int(input())

A2N = list(map(int, input().split()))
import collections
c = collections.Counter(A2N)
for i in range(1, N):
    if i in c.keys():
        print(c[i])
    else:
        print(0)
print(0)