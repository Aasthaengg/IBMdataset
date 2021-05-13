n, m, d = list(map(int, input().split()))

if d == 0:
    C = float(1/n)
else:
    C = float((2*(n-d))/(n*n))

r = C * (m-1)

print("{0:.10f}".format(r))