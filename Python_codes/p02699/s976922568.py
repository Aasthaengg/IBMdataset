a,b = map(int,input().split())
if b >= a:
    print("unsafe")
elif a > b:
    print("safe")