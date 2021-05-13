N, M = map(int, input().split())
C = []
for _ in range(N):
    A, B = map(int, input().split())
    C.append((A,B))
C.sort()
cnt = 0
res = 0
for i in range(N):
    if cnt+C[i][1]<=M:
        res += C[i][1]*C[i][0]
        cnt += C[i][1]
    else:
        break
print((M-cnt)*C[i][0] + res)