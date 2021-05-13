N = int(input())

P = list(map(int,input().split()))

ans = 0

for i in range(N):
    if P[i] == i+1:
        if i < N-1:
            now = P[i]
            P[i] = P[i+1]
            P[i+1] = now
        ans += 1
print(ans)