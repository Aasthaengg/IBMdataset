import math

n, m = map(int, input().split())
s = input()
t = input()


def lcm(x, y):
    return (x * y) // math.gcd(x, y)
l = (lcm(n, m))

sdict = {}
s_num = []
for i, moji in enumerate(list(s)):
    num = i * l // n + 1
    sdict[num - 1] = moji
    s_num.append(num - 1)

tdct = {}
t_num = []
for i, moji in enumerate(list(t)):
    num = i * l // m + 1
    tdct[num - 1] = moji
    t_num.append(num - 1)

stlst = list(set(s_num) & set(t_num))

for i in stlst:
    if sdict[i] != tdct[i]:
        print(-1)
        exit()
print(l)
