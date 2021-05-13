from itertools import combinations

N, K = map(int, input().split())
coord = sorted([tuple(map(int, input().split())) for _ in range(N)])
ans = float('inf')
for left, right in combinations(range(N), 2):
    n_points = right - left + 1
    if n_points < K: continue
    width = coord[right][0] - coord[left][0]
    y_coords = sorted([y for _, y in coord[left: right+1]])
    for i in range(n_points - K + 1):
        height = y_coords[i+K-1] - y_coords[i]
        ans = min(ans, width*height)
print(ans)