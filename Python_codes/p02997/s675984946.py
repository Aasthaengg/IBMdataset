from itertools import combinations
n, k = map(int, input().split())
if k > ((n-1)*(n-2))//2:
    print(-1)
    exit()

edges = []
for i in range(2, n+1):  # 1を中心としたスター型グラフ
    edges.append((1, i))
dist_2 = ((n-1)*(n-2))//2
list_2 = list(combinations(range(2, n+1), 2))
#print(list_2)
for i in range(dist_2-k):
    edges.append(list_2[i])


def ans(lis):
    print(len(lis))
    for x, y in lis:
        print(x, y)
ans(edges)
