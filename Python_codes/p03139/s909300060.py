n, a, b = map(int, input().split())

if a+b < n:
    max = min(a, b)
    min = 0
else:
    max = min(a, b)
    min = (a+b)-n
print(max, min)