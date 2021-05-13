a,b=map(int,input().split())
if (b-a) % 2 == 1:
    print("IMPOSSIBLE")
else:
    print((a+b)//2)