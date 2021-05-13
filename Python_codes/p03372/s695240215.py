N,C = map(int, input().split())
L = [[int(l) for l in input().split()] for _ in range(N)]

right = [0]*N
right[0] = L[0][1] - L[0][0]
for i in range(N-1):
    right[i+1] = right[i] + L[i+1][1] - (L[i+1][0] - L[i][0])

left = [0]*N
left[N-1] = L[N-1][1] - (C - L[N-1][0])
for i in range(N-1, 0, -1):
    left[i-1] = left[i] + L[i-1][1] - (L[i][0] - L[i-1][0])

Right = [0]*(N+1)
for i in range(N):
    Right[i+1] = max(right[i], Right[i])
Left = [0]*(N+1)
for i in range(N, 0, -1):
    Left[i-1] = max(left[i-1], Left[i])

ans = max(0, max(right), max(left))
for i in range(N-1, -1, -1):
    ans = max(ans, Right[i] + left[i] - (C - L[i][0]))
for i in range(N):
    ans = max(ans, Left[i+1] + right[i] - L[i][0])

print(ans)