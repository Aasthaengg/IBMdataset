a, b, c = map(int, input().split())

t1 = abs(a//2 * b * c - ((a - a//2) * b * c))
t2 = abs(b//2 * a * c - ((b - b//2) * a * c))
t3 = abs(c//2 * b * a - ((c - c//2) * b * a))
print(min(t1, t2, t3))
