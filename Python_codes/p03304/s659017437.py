n, m, d = map(long, raw_input().split())
c = n if d == 0 else 2 * (n -d)
print float(c)*(m-1)/n**2

