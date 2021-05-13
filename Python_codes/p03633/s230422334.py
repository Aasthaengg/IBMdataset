def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a
    
n = int(input())
s = 1
for i in range(n):
    x = int(input())
    s = s // gcd(s, x) * x
print(int(s))