import bisect
n, k, c = map(int, input().split())
s = input()
a = []
for i in range(n):
    if s[i] == 'o':
        a.append(i+1)

m = len(a)
l = [0 for _ in range(m)]
r = [0 for _ in range(m)]

cur = 0
l[0] = a[0]
while True:
    to = bisect.bisect_left(a, a[cur] + c + 1)
    if to == m:
        break
    l[to] = l[cur] + 1
    cur = to

for i in range(m-1):
    if l[i] > l[i+1]:
        l[i+1] = l[i]

#print(l)

r[m-1] = 1
cur = m-1
while True:
    to = bisect.bisect_left(a, a[cur] - c) - 1
    if to == -1:
        break
    r[to] = r[cur] + 1
    cur = to

for i in range(m-1):
    x = m - 2 - i
    if r[x] < r[x+1]:
        r[x] = r[x+1]

#print(r)
l = [0] + l
r = [r[0]] + r + [0]

for i in range(1, m+1):
    if l[i-1] + r[i+1] < k:
        print(a[i-1])