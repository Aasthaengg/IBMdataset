d = int(input())

if d % 1000 == 0:
    print(0)
else:
    print(1000 - d % 1000)