def GCD(a,b):
    if b == 0:
        return a
    else:
        r = a % b
        return GCD(b, r)
        
while True:
    try:
        data = map(int, raw_input().split())
    except:
        break
    if data[0] > data[1]:
        a = data[0]
        b = data[1]
    else:
        a = data[1]
        b = data[0]
    x = GCD(a, b)
    y = a*b / x
    
    print x, y