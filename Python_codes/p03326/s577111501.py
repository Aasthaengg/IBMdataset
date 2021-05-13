n,m = map(int,input().split())
xyz = [list(map(int,input().split())) for i in range(n)]
ans = 0
for i in range(8):
    s = [0 for j in range(n)]
    for j in range(n):
        a = 0
        for k in range(3):
            if i>>k&1:
                a += xyz[j][k]
            else:
                a -= xyz[j][k]
        s[j] = a
    s.sort()
    ans = max(ans,sum(s[n-m:]))
print(ans)