a, b, c, d = map(int, input().split())
 
def gcd(x, y):
    if x < y:
        x, y = y, x
    while True:
        if x % y == 0:
            return y
        x, y = y, x%y
 
x = b - a + 1
cx = b // c - (a-1) // c
dx = b // d - (a-1) // d
cdx = b // (c*d // gcd(c, d)) - (a-1) // (c*d // gcd(c, d))
print(x - cx - dx + cdx)