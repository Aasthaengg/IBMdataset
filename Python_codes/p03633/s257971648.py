def gcd(a, b):
    if(a == 0):
        return b
    return gcd(b % a, a)
def lcm(a, b):
    return a // gcd(a, b) * b
t = int(input())
ans = 1
while(t != 0):
    t -= 1
    n = int(input())
    ans = lcm(ans, n)
print(int(ans))
