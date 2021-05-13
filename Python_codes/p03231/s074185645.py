N,M = map(int, input().split())
S = input()
T = input()

def gcd(v1, v2):
    if v2 == 0:
        return v1
    return gcd(v2, v1%v2)

def lcm(v1,v2):
    return v1 * v2 // gcd(v1,v2)

my_gcd = gcd(N,M)
s_ = S[::N//my_gcd]
t_ = T[::M//my_gcd]
if s_ == t_:
    print(lcm(N,M))
else:
    print(-1)
