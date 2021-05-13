n,a,b = map(int,input().split())
if a <= b:
    print(max(0,(b * (n - 1) + a) - (a * (n - 1) + b) + 1))
elif a > b:
    print("0")