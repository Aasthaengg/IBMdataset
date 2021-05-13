N = int(input())
P = list(map(int, input().split()))

mins = [P[i] for i in range(N)]

for i in range(1, N):
    if mins[i] > mins[i-1]:
        mins[i] = mins[i-1]


ans = 1
for i in range(1, N):
    if mins[i-1] >= P[i]:
        ans += 1

print(ans)