N, M = map(int, input().split())
py = []
for i in range(M):
    p, y = map(int, input().split())
    py += [[i, p, y]]
py = sorted(py, key=lambda x:(x[1], x[2]))
cnt = 0
pre = py[0][1]
ans = []
for n, p, y in py:
    if pre != p:
        cnt = 1
        pre = p
    else:
        cnt += 1
        
    ans += [[n, str(p).zfill(6)+str(cnt).zfill(6)]]

ans = sorted(ans, key=lambda x:x[0])
for _, n in ans:
    print(n)
