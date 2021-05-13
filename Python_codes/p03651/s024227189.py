def gcd_(a, b):
    if a < b:  a, b = b, a
    if b == 0:  return a
    return gcd_(b, a % b)

def gcd(l):
    ans = l[0]
    for i in l:  ans = gcd_(ans, i)
    return ans

def cin():
    in_ = list(map(int,input().split()))
    if len(in_) == 1:  return in_[0]
    else:  return in_

def solve():   
    if N == 1:  return A == K    
    g = gcd(A)
    m = max(A)
    return K <= m and K % g == 0

N, K = cin()
A = cin()
ret = solve()
if ret:  print("POSSIBLE")
else:  print("IMPOSSIBLE")