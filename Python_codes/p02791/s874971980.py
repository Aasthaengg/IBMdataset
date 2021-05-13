n = int(input())
P = list(map(int, input().split()))
P_min = P[0]
cnt = 1

for i in range(n):
    if P_min > P[i]:
        cnt += 1
        P_min = P[i]
print(cnt)