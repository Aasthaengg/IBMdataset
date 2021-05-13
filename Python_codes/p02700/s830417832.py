a, b, c, d = map(int,input().split())
for i in range(100):
    if c > b:
        c -= b
        
    elif c <= b:
        print("Yes")
        exit()
        
    if a > d:
        a -= d
        
    elif a <= d:
        print("No")
        exit()