from itertools import combinations

n = int(input())
D = list(map(int, input().split()))

xy = list(combinations(D,2))
ans = 0

for i in range(len(xy)):
    ans += xy[i][0]*xy[i][1]

print(ans)
