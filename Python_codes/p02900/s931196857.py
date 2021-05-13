def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)
ans = 1
def fact(n):
    global ans
    p = 2
    while p**2 <= n:
        flag = False
        while n%p == 0:
            flag = True
            n /= p
        p += 1
        if flag:
            ans += 1
    if n!= 1:
        ans += 1
a,b = map(int, input().split())
g = gcd(a,b)
fact(g)
print(ans)