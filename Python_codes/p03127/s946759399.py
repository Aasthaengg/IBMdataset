# 最大公約数
def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a


n = int(input())
a = list(map(int,input().split()))

ans = 0
for i in a:
    ans = gcd(ans,i)
print(ans)