N, X = map(int, input().split())
m = sorted(int(input()) for i in range(N))
cnt = 0 
for i in range(N):
    if m[i] < X:
        X = X - m[i]
        cnt += 1
cnt += X//m[0]
print(cnt)