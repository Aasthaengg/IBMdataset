a, b, c = map(str, input().split())
r = 'YES' if a[-1] == b[0] and b[-1] == c[0] else 'NO'
print(r)