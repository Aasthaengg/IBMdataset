n, m, d = map(int, input().split())
a1 = (n-d)*(m-1)
if d != 0:
  a1 *= 2

a2 = n**2
ans = a1 / a2
print(ans)