a,b = map(int, input().split())

k = (a**2-b**2)/(2*(a-b))

if k.is_integer() == False:
    print("IMPOSSIBLE")
else:
    print(int(k))