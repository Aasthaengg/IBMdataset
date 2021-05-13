from sys import stdin
 
x, y = [int(x) for x in stdin.readline().rstrip().split()]
 
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
 
print(gcd(x, y))
