import collections
n,m = map(int, input().split())
hy = map(int, input().split())
h = list(hy)
count = [0]*n
for _ in range(m):
    a,b = map(int, input().split())
    if h[a-1] > h[b-1]:
        count[b-1] = 1
    if h[a-1] < h[b-1]:
        count[a-1] = 1
    if h[a-1] == h[b-1]:
        count[a-1] = 1
        count[b-1] = 1
c = collections.Counter(count)
print(c[0])
