n, a, b = map(int, input().split())
H = [int(input()) for _ in range(n)]

def is_ok(x):
    cnt = 0
    for i in range(n):
        h  = H[i]
        if h <= x*b:
            continue
        else:
            h -= x*b
            cnt += (h+(a-b-1))//(a-b)
    if cnt <= x:
        return True
    else:
        return False

l = 0
r = 19**18
while l+1 < r:
    c = (l+r)//2
    if is_ok(c):
        r = c
    else:
        l = c
print(r)
