import collections

n = int(input())
a = list(map(int, input().split()))

b = collections.deque()
for i in range(len(a)):
    if i % 2 == 0:
        b.append(a[i])
    else:
        b.appendleft(a[i])

b = list(b)
if n % 2 == 1:
    b.reverse()

print(" ".join([str(x) for x in b]))
