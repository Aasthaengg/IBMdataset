n, a, b = map(int, input().split())
mn = None
mx = None

mx = min(a, b)

if n >= a+b:
    mn = 0
else:
    mn = a+b-n

print(mx, mn)