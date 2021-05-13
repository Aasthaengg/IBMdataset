from itertools import combinations
N, X, Y = map(int, input().split())
N_lst = [i for i in range(1, N + 1)]
michi = combinations(N_lst, r = 2)
dis = [0 for _ in range(N + 1)]
for i,j in michi:
    seiki = j - i
    betsu = abs(j-Y) + 1 + abs(X-i)
    if seiki <= betsu:
        dis[seiki] += 1
    else:
        dis[betsu] += 1
for h in range(1, N):
    print(dis[h])