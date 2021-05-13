a,b = map(int, input().split())
if abs(a-b) > a:
    print(a)
else:
    if a%b == 0:
        print(0)
    else:
        print(abs(a%b-b))