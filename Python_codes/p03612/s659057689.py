N = int(input())
P = [0] + list(map(int, input().split()))

cnt = 0
for i in range(1, N + 1):
    if i == P[i]:
        cnt += 1
        if i != N:
            P[i + 1], P[i] = P[i], P[i + 1]
        else:
            P[i - 1], P[i] = P[i], P[i - 1] 

print(cnt)