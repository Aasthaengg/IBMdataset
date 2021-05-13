N, X = map(int, input().split())
M = [int(input()) for i in range(N)]
cnt = N
X -= sum(M)
cnt += X // min(M)
print(cnt)
