N = int(input())
A = list(map(int,input().split()))
 
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
 
def lcm(a, b):
    return (a * b)//gcd(a,b)
 
lcm_a = 1
 
for i in range(N):
    lcm_a = lcm(lcm_a,A[i])
 
ans = 0
for i in range(N):
    ans += lcm_a//A[i]
 
mod = int(1e9+7)
 
print(ans%mod)