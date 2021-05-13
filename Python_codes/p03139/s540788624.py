n, a, b = map(int, input().split())

ma = min(a,b)
mi = max(0, a+b-n)
print(str(ma) + ' ' + str(mi))