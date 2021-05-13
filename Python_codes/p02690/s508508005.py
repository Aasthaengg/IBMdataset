import sys

x = int(input())
for a in range(0,1000):
    a_5 = a**5
    if a_5 > x:
        b = 0
        s = x+1
        while s > x:
            s = a_5 - b**5
            if s == x:
                print(a, b)
                sys.exit()
            b += 1
            
    elif a_5 < x:
        b = 0
        s = x-1
        while s < x:
            s = a_5 - b**5
            if s == x:
                print(a, b)
                sys.exit()
            b -= 1
    else:
        print(a,0)
        sys.exit()