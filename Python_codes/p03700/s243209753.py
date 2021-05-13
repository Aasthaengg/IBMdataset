n, a, b = map(int, input().split())
H = [int(input()) for _ in range(n)]

def ok(x):
    tot = 0
    for i in range(n):
        if b*x >= H[i]:
            continue
        else:
            r = H[i] - b*x
            if r%(a-b) == 0:
                tot += r//(a-b)
            else:
                tot += r//(a-b)+1
    if tot <= x:
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