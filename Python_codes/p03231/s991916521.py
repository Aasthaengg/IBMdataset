# a,bの最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# a,bの最小公倍数
def lcm(a, b):
    return a * b // gcd(a, b)


n,m = map(int,input().split())
s = input()
t = input()

lc = lcm(n,m)

dic = {}

for i in range(len(s)):
    dic[lc//n*i] = s[i]
for i in range(len(t)):
    if lc//m*i in dic:
        if dic[lc//m*i] != t[i]:
            print(-1)
            exit()

print(lc)