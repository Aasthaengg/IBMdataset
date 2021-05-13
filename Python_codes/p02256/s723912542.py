X, Y = map(int, input().split())

def gcd(_x, _y) :
    x = min(_x, _y)
    y = max(_x, _y)
    
    if x == 0 or y == 0 :
        return 0
    if x == y :
        return X
    elif y % x == 0 :
        return min(x, y)
    elif y % x != 0 :
        return gcd(y % x, x)
        
print(gcd(X, Y))
