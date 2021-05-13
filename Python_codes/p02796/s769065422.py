N = int(input())

R = []

for i in range(N):
    x, l = map(int, input().split())
    R.append((x-l,x+l))

R_sorted = sorted(R, key=lambda x:x[1])

ans = 0
right = -10**9 - 1
i = 0
while(i < N):
    left = R_sorted[i][0]
    if left >= right:
        ans += 1
        right = R_sorted[i][1]
    i += 1

print(ans)