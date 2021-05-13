N, X = map(int,input().split())
LL = list(map(int, input().split()))

mj = 0
cnt = 1
for i in range(N):
    mj += LL[i]
    if mj <= X:
        cnt += 1

print(cnt)