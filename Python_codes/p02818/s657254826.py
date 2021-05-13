a,b,k = map(int,input().split())
if a+b <= k:
    print("0 0")
    exit()
if a <= k:
    b = b - k + a
    a = 0
    print(a,b)
else:
    print(a-k,b)