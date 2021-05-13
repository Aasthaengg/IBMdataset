import fractions
k = list(map(int, input().split()))

def lcm(k):
    ans = k[0]
    for i in range(1, len(k)):
        ans = ans * k[i] // fractions.gcd(ans, k[i])
    return ans
  
print(lcm(k))