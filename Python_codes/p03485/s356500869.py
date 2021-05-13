a, b = list(map(int, input().split()))

avg = (a + b) / 2
if avg % 1 == 0:
    print(int(avg))
else:
    print(int(avg + 1))