from collections import Counter

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

pq = []

for x, y in A:
    for i, j in A:
        if x == i and y == j:
            continue
        pq.append(str(i-x)+str(j-y))

ans = Counter(pq).most_common()

if ans == []:
    print(1)
else:
    print(N - ans[0][1])