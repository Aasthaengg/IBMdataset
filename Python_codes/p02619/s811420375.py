d = int(input())
c = list(map(int , input().split()))
s = [list(map(int , input().split())) for _ in range(d)]

ans = 0
last = [0] * 26
for di in range(1, d+1):
    ti = int(input()) - 1
    last[ti] = di
    for i in range(26):
        ans -= (di - last[i]) * c[i]
    ans += s[di-1][ti]
    print(ans)
