n = int(input())
a = list(map(int, input().split()))
sa = sum(a)

b = [1]
f = True
for i in range(n+1):
    sa -= a[i]
    d = min(sa, (b[i] - a[i]) * 2)
    if d < 0:
        f = False
        break
    b.append(d)

print(sum(b) if f else -1)
