n,a,b = map(int,input().split())
h = []
for i in range(n):
    h.append(int(input()))

def hantei(c):
    tmp = 0
    for i in range(n):
        tmp += max(0, -(-(h[i] - b * c) // (a-b)))
    if tmp <= c:
        return True
    else:
        return False

l = 0
r = 10**18+10

while r - l > 1:
    c = (l + r) // 2
    tmp = 0
    for i in range(n):
        tmp += max(0, -(-(h[i] - b * c) // (a-b)))
    if hantei(c):
        r = c
    else:
        l = c

if hantei(l):
    print(l)
else:
    print(r)
