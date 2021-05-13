N, M = map(int, input().split())
I = [list(map(int, input().split())) for _ in range(M)]
s = [0] * M
c = [0] * M
for i in range(M):
    s[i] = I[i][0]
    c[i] = I[i][1]
ans = -1
if N == 1:
    for i in range(0, 10):
        flg = 0
        for j in range(M):
            if c[j] != i:
                flg = 1
                break
        if flg == 1:
            continue
        if ans == -1:
            ans = i
        else:
            ans = min(ans, i)
else:
    for i in range(10**(N-1), 10**N):
        i = str(i)
        flg = 0
        for j in range(M):
            if i[s[j]-1] == str(c[j]):
                continue
            flg = 1
            break
        if flg == 1:
            continue
        if ans == -1:
            ans = int(i)
        else:
            ans = min(ans, int(i))

print(ans)