n = int(input())

a = list(input().split())

e = []
o = []

for i in range(n):
    if i%2 == 0:
        e.append(a[i])
    else:
        o.append(a[i])

if n%2 == 0:
    o = o[::-1]
    ans = o + e
    print(" ".join(ans))
else:
    e = e[::-1]
    ans = e + o
    print(" ".join(ans))