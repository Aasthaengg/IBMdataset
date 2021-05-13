from itertools import accumulate

n, q = map(int, input().split())
s = input()

t = [0] * n
for i in range(n - 1):
    if s[i] + s[i + 1] == "AC":
        t[i] = 1

a = [0] + list(accumulate(t))
for i in range(q):
    l, r = map(int, input().split())
    print(a[r - 1] - a[l - 1])