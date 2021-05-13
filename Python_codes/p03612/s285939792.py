N = int(input())
P = list(map(int, input().split()))


ans = 0

for i in range(N):
    if P[0] == 1:
        ans += 1
        P[0], P[1] = P[1], P[0]
    elif i != N-1:
        if P[i] == i+1:
            ans += 1
            P[i+1], P[i] = P[i], P[i+1]
    elif i == N-1:
        if P[i] == i+1:
            ans += 1

print(ans)