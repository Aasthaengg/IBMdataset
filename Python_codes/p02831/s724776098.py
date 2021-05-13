
def gcd(a,b):
    ma = max(a,b)
    mi = min(a,b)
    while(True):
        los = ma % mi
        ma = mi
        mi = los
        if los == 0:
            result = ma
            break
    return result

a,b = map(int,input().split())
print(a*b//gcd(a,b))