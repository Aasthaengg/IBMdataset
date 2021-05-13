N, C, K = map(int, input().split())
T = []
for i in range(N):
    t = int(input())
    T.append(t)
T.sort()

cnt = 0
res = 1
time = T[0]
for i in range(N-1):
    cnt += 1
    if cnt == C or time + K < T[i+1]:
        res += 1
        cnt = 0
        time = T[i+1]
print(res)