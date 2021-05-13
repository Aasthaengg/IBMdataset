N, X = map(int, input().split())
L = list(map(int, input().split()))

cnt = 1
p = 0
for i in range(N):
    p += L[i]
    if p <= X:
        cnt += 1

print(cnt)