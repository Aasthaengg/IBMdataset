n, a, b = map(int, input().split())
if a+b>=n:
    c = a+b-n
else:
    c = 0
print(min(a,b), c)
