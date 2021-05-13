n, m = map(int,input().split())
ab = []
for i in range(n):
    ab.append(list(map(int,input().split())))

ab = sorted(ab, key=lambda x:(x[0], x[1]))

cost = 0
while m > 0:
    a, b = ab.pop(0)
    if b > m:
        cost += m * a
        m = 0
    else:
        cost += b * a
        m -= b
print(cost)