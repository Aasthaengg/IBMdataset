

n = int(input())
p = list(map(int, input().split()))

def swap():
    cnt = 0
    for i in range(n):
        if i+1 == p[i]:
            if i+1 < n:
                p[i], p[i+1] = p[i+1], p[i]
            else:
                p[i-1], p[i] = p[i], p[i-1]
            cnt += 1
    return cnt

ok = True
ans = 0
while True:
    ans += swap()
    for i in range(n):
        if p[i] == i+1:
            ok = False
    if ok:
        print(ans)
        exit()