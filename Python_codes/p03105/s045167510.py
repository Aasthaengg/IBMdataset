a, b, c = map(int, input().split())
if a > b:
    print(0)
elif a == b:
    print(1)
elif a < b:
    if b // a <= c:
         print( b // a)
    else:
         print(c)