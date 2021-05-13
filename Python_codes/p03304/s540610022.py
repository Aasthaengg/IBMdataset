n, m, d = map(int, input().split())

if d != 0:
    diff = 2 * (n - d)
else:
    diff = n
diff = diff/float(n)

print(diff/float(n) * (m - 1))