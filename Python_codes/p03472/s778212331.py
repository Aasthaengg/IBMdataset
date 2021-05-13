import math as m1
n, h = map(int, input().split())
a, b = [], []
for i in range(n):
    a_, b_ = map(int, input().split())
    a.append(a_)
    b.append(b_)
b = list(reversed(sorted(b)))
m = max(a)
ans = 0
for i in b:
    if i > m:
        if h - i <= 0:
            print(ans + 1)
            exit()
        h -= i
        ans += 1
print(ans + m1.ceil(h / m))