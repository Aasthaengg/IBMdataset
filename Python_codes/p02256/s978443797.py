def gcd(b, s):
    mod = b % s
    if mod != 0:
        return gcd(s, mod)
        
    else:
        return s

x, y = map(int, input().split())
b = max(x, y)
s = min(x, y)
a = gcd(b, s)
print(a)