def cin():  return list(map(int,input().split()))

def gcd_(a, b):
    if a < b:  a, b = b, a
    if b == 0:  return a
    return gcd_(b, a % b)

def gcd(l):
    ans = 0
    for i in l:  ans = gcd_(ans, i)
    return ans

def lcm_(x,y):
    return (x * y) // gcd_(x, y)

def lcm(l):
    ans = l[0]
    for i in l:  ans = lcm_(ans, i)
    return ans

N = cin()[0]
v = cin()
lc = lcm(v)
ans = 0
INF = 10 ** 9 + 7
lc %= INF
for i in range(N):
    ans += lc * pow(v[i], INF - 2, INF)
    ans %= INF
print(int(ans))