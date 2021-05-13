a, b = map(int, input().split())
SUM = 0
if b < a:
    
    for i in range(a):
        SUM = SUM + (10**i) * b
    print(str(SUM))
elif a < b:
    for i in range(b):
        SUM = SUM + (10**i) * a
    print(str(SUM))
else:
    for i in range(a):
        SUM = SUM + (10**i) * a
    print(str(SUM))