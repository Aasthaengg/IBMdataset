a, b, c = map(int, input().split())

a1 = a//2
a2 = a - (a//2)
b1 = b//2
b2 = b - (b//2)
c1 = c//2
c2 = c - c//2

ans = min(a2*b*c - a1*b*c, b2 * a*c - b1*a*c)
ans = min(ans, c2 * a*b - c1 * a * b)
print(ans)
