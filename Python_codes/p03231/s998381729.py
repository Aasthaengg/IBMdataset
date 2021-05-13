def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

#a,bの最小公倍数
def lcm(a, b):
	return a * b // gcd (a, b)
n,m = map(int,input().split())
s = input()
t = input()
mx = max(n,m)
mn = min(n,m)
if mx / mn % 1 == 0:
    c = mx//mn
    if mn == len(s):
        if s == t[::c]:
            print(t[::c])
            print(mx)
        else:
            print(-1)
    else:
        if t == s[::c]:
            print(s[::c])
            print(mx)
        else:
            print(-1)
else:
    num = lcm(n,m)
    mmx = num // mx
    mmn = num // mn
    ber = lcm(mmx,mmn)
    if mn == len(s):
        if s[::ber//mmn] == t[::ber//mmx]:
            print(num)
        else:
            print(-1)
    else:
        if s[::ber//mmx] == t[::ber//mmn]:
            print(num)
        else:
            print(-1)