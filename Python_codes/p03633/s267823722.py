def cin():
    in_ = list(map(int,input().split()))
    if len(in_) == 1:  return in_[0]
    else:  return in_

def gcd_(a, b):
    if a < b:  a, b = b, a
    if b == 0:  return a
    return gcd_(b, a % b)

def gcd(l):
    ans = l[0]
    for i in l:  ans = gcd_(ans, i)
    return ans

def lcm_(x,y):
    return (x * y) // gcd_(x, y)

def lcm(l):
    ans = l[0]
    for i in l:  ans = lcm_(ans, i)
    return ans

N = cin()
a = [cin() for _ in range(N)]
print(lcm(a))