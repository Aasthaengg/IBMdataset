n = int(input())
t = [int(input()) for _ in range(n)]

def gcd(a,b):
    if b == 0:
        return a
    return gcd (b, a%b)

#2数の積/最大公約数=最小公倍数
def lcm(a,b):
    return a*b//gcd(a,b)

if n == 1:
    print(t[0])
    exit(0)
ans = lcm(t[0], t[1])
for i in range(1, n-1):
    ans = lcm(ans, t[i+1])
print(ans)