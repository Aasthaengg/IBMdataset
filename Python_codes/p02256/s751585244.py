a,b = map(int,input().split())
def gcd(x,y):
    q = max(x,y)  %  min(x,y)
    if q == 0 :
        return [min(x,y),0]
    return gcd(min(x,y),q)

print(max(gcd(a,b)))

