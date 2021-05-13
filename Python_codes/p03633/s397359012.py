# 最大公約数
def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a

# 最小公倍数

def lcm(a,b):
    return a*b // gcd(a,b)

n = int(input())

for i in range(n):
    t = int(input())
    if i != 0:
        ans = lcm(ans,t)
    else:
        ans = t
    #print(ans)
print(ans)