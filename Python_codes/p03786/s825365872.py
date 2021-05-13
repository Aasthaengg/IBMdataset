N = int(input())
A = sorted([int(x) for x in input().split()])

color_min = 0
creature_size = A[0]

for i in range(1, N):
    if 2 * creature_size >= A[i]:
        creature_size += A[i]
    else:
        color_min = i
        creature_size += A[i]

ans = N - color_min

print(ans)