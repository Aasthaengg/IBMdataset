
N, C = map(int, input().split())
stc = [list(map(int, input().split())) for _ in range(N)]
 
record = [[0] * 10 ** 5 for _ in range(C)]
for s, t, c in stc:
    for i in range(s, t + 1):
        record[c-1][i-1] = 1
 
ans = 0
for i in range(10 ** 5):
    cnt = 0
    for j in range(C):
        cnt += record[j][i]
    ans = max(ans, cnt)
 
print(ans)