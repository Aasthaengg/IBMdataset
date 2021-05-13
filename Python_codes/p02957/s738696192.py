a,b=map(int, input().split())
if ((a+b)/2).is_integer():
    print((a+b)//2)
else:
    print("IMPOSSIBLE")