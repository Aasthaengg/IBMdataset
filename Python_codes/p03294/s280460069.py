n = int(input())
a = list(map(int, input().split()))
a.sort()
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
def lcm(a, b):
    return (a*b)//gcd(a, b)
llcm = 1
for i in a:
    llcm = lcm(llcm, i)
ans = 0
for i in a:
    ans += (llcm-1)%i
print(ans)