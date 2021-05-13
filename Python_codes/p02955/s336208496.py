N, K = list(map(int, input().split()))
As = list(map(int, input().split()))
rs = []
a = sum(As)
for i in range(a):
    i += 1
    if a % i == 0:
        rs.append(i)
        rs.append(a//i)
    if a < i**2:
        break
rs = sorted(rs)[::-1]
for r in rs:
    Bs = sorted([A%r for A in As])
    sum1 = 0
    sum2 = r*N - sum(Bs)
    R = None
    for b in Bs:
        sum1 += b
        sum2 -= r - b
        if abs(sum1 - sum2) % r == 0:
            if max(sum1, sum2) > K:
                continue
            R = r
            break
    if R:
        break
print(R)
