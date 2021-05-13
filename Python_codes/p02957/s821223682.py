a, b = map(int, input().split())
c = a+b
if c%2==0:
    print((a+b)//2)
else:
    print("IMPOSSIBLE")