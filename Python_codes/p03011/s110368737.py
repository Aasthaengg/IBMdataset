p, q, r = map(int, input().split())
m = p + q
if m > min(q + r, r + p):
    m = min(q + r, r + p)
print(m)