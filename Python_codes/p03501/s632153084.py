n, a, b = map(int, input().split())
time = n * a
if time < b:
    print(time)
else:
    print(b)