a,b,c = (int(x) for x in input().split())


result = b + c - a

if result <= 0:
    print(0)
else:
    print(result)