from math import factorial as fa
def comb(n, r):
    return fa(n)//(fa(n-r)*fa(r))
n, p = map(int, input().split())
A = list(map(lambda x:int(x)%2, input().split()))
even = A.count(0)
odd = A.count(1)
ans = 0
for i in range(p,odd+1,2):
    ans += comb(odd, i)
print(ans*pow(2,even))