a, b = map(int, input().split())
start = a+b
if start >= 24:
    start = start - 24

print(start)