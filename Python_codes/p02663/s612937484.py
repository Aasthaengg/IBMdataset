a, b, c, d, e = map(int, input().split())
time = (c * 60 + d) - (a * 60 + b)
time = time + 24 * 60 if time < 0 else time
print((60 * c + d) - (60 * a + b) - e)