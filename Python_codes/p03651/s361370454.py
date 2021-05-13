n,k = map(int,input().split())

al = list(map(int,input().split()))


# a,bの最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# a,bの最小公倍数
def lcm(a, b):
    return a * b // gcd(a, b)


ans = al[0]

for a in al:
    ans = gcd(a, ans)

if k % ans == 0 and k <= max(al):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")