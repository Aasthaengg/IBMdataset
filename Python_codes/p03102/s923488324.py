N, M, C = map(int, input().split())
B = list(map(int, input().split()))
cnt = 0
for _ in range(N):
    S = C
    for i, a in enumerate(map(int, input().split())):
        S += a*B[i]
    if S>0:
        cnt += 1
print(cnt)