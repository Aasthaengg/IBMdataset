n = int(input())
m, sec = divmod(n, 60)
hr, m = divmod(m, 60)
print(hr, m, sec, sep=':')