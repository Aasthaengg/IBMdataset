n, m, d = input().split()
n, m, d = float(n), float(m), float(d)
if d < 0.5:
    print((n-d) * (m-1) / n**2)
else:
    print(2*(n-d)*(m-1) / n**2)