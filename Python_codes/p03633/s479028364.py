N = int(input())
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)
def lcm(a,b):
    return a*b//gcd(a,b)

T = [int(input()) for _ in range(N)]
ans = T[0]
for e in T:
    ans = lcm(e,ans)
print(ans)
