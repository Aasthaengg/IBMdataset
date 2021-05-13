a,b = [int(x) for x in input().split()]
if a>b:
    print(a-1)
else:
    print(min([a,b]))