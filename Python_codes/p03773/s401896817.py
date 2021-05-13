x, y = map(int, input().split())
time = x + y
if time < 24:
    print(str(time))
else:
    print(str(time - 24))