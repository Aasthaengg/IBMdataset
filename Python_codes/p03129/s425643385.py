h, w = map(int, input().split())
if h%2==0:
    a=h//2
    if a>=w:
        print("YES")
    else:
        print("NO")
else:
    a=h//2+1
    if a>=w:
        print("YES")
    else:
        print("NO")