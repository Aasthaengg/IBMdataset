import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = [int(_) for _ in input().split()]
cb = [0] * m
for i in range(m):
    bb, cc = map(int, input().split())
    cb[i] = (cc, bb)

cb.sort(reverse=True)

arr = []
l = 0
for i in range(m):
    if l + cb[i][1] > 10**5:
        add = 10**5 - l
        for j in range(add):
            arr.append(cb[i][0])
        break
    else:
        for j in range(cb[i][1]):
            arr.append(cb[i][0])
        l += cb[i][1]

a = a + arr
a.sort(reverse=True)
print(sum(a[0:n]))