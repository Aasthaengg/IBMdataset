n = int(input())
L = list(map(int, input().split()))

from itertools import combinations

cnt = 0
for i in combinations(L, 3):
    longest = max(i)
    rest = sum(i) - max(i)
    if longest < rest and i[0] != i[1] and i[0] != i[2] and i[1] != i[2] :
        cnt += 1
print(cnt)