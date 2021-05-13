n, m = map(int, input().split())
s = [list(map(int, input().split())) for i in range(m)]
p = list(map(int, input().split()))

ans = 0
for i in range(2**n): #スイッチの状態
    cnt = 0
    for j in range(m): #電球の状態
        s_on = 0
        for k in range(s[j][0]):
            s_on += (i >> (s[j][k+1]-1) & 1)
        if s_on % 2 == p[j]:
            cnt += 1
    if cnt == m:
        ans += 1

print(ans)