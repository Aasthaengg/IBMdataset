n, a, b = map(int, input().split())
H = [int(input()) for i in range(n)]

def ok(x):
    t = 0
    for i in range(n):
        h = H[i]
        res = h-b*x
        if res <= 0:
            continue
        else:
            if res%(a-b) == 0:
                t += res//(a-b)
            else:
                t += res//(a-b)+1
    if t <= x:
        return True
    else:
        return False

l = 0
r = 10**10
while l+1 < r:
    c = (l+r)//2
    if ok(c):
        r = c
    else:
        l = c
print(r)