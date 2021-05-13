n, a, b = map(int, input().split())
x = [int(i) for i in input().split()]
c = 0
s = x[0]
for t in x[1:]:
    c += min((t - s) * a, b)
    s = t
print(c)