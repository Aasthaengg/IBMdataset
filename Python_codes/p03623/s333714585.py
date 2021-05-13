x, a, b = map(int, input().split())
l_a = abs(x-a)
l_b = abs(x-b)
r = 'A' if l_a < l_b else 'B'
print(r)