a, b = map(int, input().split())
 
if 1 <= a <= 9:
    if 1 <= b <= 9:
        print(a * b)
    else:
        print(-1)
else:
    print(-1)