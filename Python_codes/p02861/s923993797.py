from itertools import permutations
N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
ans = 0
li = list(permutations(range(N)))
l = len(list(permutations(range(N))))
for i in li:
    for j in range(N-1):
        x1, x2 = xy[i[j]][0], xy[i[j+1]][0]
        y1, y2 = xy[i[j]][1], xy[i[j+1]][1]
        ans += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
print(ans/l)