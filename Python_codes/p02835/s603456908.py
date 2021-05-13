a,b,c=map(int, input().split())
ans = a + b + c
if ans > 21:
    print("bust")
else:
    print("win")