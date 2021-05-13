n,k = map(int,input().split())
a = list(map(int,input().split()))
f = list(map(int,input().split()))

def hantei(c):
    tmp = 0
    for i in range(n):
        if af[i] > c:
            a1 = c // f[i]
            tmp += a[i]- a1
    if tmp <= k:
        return True
    else:
        return False

hq = []

a.sort()
f.sort(reverse = True)

af = []
for i in range(n):
    af.append(a[i] * f[i])

l = 0
r = 10**12+10

while r - l > 1:
    c = (l + r) // 2
    if hantei(c):
        r = c
    else:
        l = c

if hantei(l):
    print(l)
else:
    print(r)
