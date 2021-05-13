N, M = map(int, input().split())
k = []*M
s = []*M
for i in range(M):
    inp = list(map(int, input().split()))
    k.append(inp[0])
    s.append(inp[1:])
p = list(map(int, input().split()))

ans = 0
for i in range(0,2**N):
    n = format(i,'010b')
    for j in range(M):
        pj = 0
        for k in range(len(s[j])):
            pj += int(n[10-s[j][k]])
        if p[j] != pj%2:
            break
        if j == M-1:
            ans += 1

print(ans)