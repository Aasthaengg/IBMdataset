from sys import stdin

n, k, q = map(int, stdin.readline().rstrip().split())
a = [0] * q
for i in range(q):
    a[i] = int(stdin.readline().rstrip())

l = [0] * (n+1)

for ai in a:
    l[ai] += 1

for i in range(n):
    j = i+1
    point = k - (q-l[j])
    if point <= 0:
        print('No')
    else:
        print('Yes')