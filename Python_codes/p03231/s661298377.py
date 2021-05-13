n, m = map(int, input().split())
s, t = list(input()), list(input())


def gcd(a, b):
    if a > b:
        return gcd(b, a)
    while a > 0:
        a, b = b % a, a
    return b


def lcm(a, b):
    return a * b // gcd(a, b)


l = lcm(len(s), len(t))
x = {}  # これふつうにリストだとREになるのマジで謎なんだけど
for i in range(0, len(s)):
    x[i * (l // len(s))] = s[i]
for i in range(0, len(t)):
    if i * (l // len(t)) not in x:
        continue
    else:
        if x[i * (l // len(t))] != t[i]:
            print(-1)
            exit()
print(l)