def gcd(x, y):
    if x == y:
        return x
    while(1):
        if x < y:
            temp = x
            x = y
            y = temp
        x = x%y
        if x == 0:
            return y
            
x, y = map(int, raw_input().split())

print gcd(x, y)