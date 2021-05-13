N, C, K = map(int, input().split())
T = [0 for _ in range(N)]
for i in range(N):
    T[i] = int(input())
T = sorted(T)

flag = 0
cnt = 0
ans = 0
for i in range(len(T)):
    time = T[i] - T[flag]
    cnt += 1
    if time > K or cnt > C:
        flag = i
        cnt = 1
        ans += 1
print(ans + 1)
