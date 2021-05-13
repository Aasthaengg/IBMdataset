a,b = (int(x) for x in input().split())

result = a - b * 2

if result <= 0:
    print(0)
else:
    print(result)