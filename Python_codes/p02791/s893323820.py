N = int(input())
P = list(map(int, input().split()))

n = P[0]
cnt = 1
for i in range(1,N):
    if P[i] <= n:
        cnt += 1
        n = P[i]
print(cnt)