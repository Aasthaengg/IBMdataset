def GCD(x, y):
    if(x == 0):
        return(y)
    return(GCD(y % x, x))

def LCM(x, y):
    return(x * y / GCD(x, y))

while(True):
    try:
        a = map(int, raw_input().split())
        if(a[0] > a[1]):
            a[0], a[1] = a[1], a[0]
        print(GCD(a[0], a[1])),
        print(LCM(a[0], a[1]))
    except Exception:
        break