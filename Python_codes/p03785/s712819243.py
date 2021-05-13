N, C, K = map(int, input().split())
T = []
for _ in range(N):
    T.append(int(input()))
T.sort()

ans = 1
temp = [T[0], 0]
for t in T:
    if temp[0] + K < t or temp[1] + 1 > C:
        ans += 1
        temp = [t, 0]
    temp[1] += 1
print(ans)