import copy
n = int(input())

ans = 0
def warshall_floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == k or j == k:
                    continue
                elif d[i][j] > d[i][k] + d[k][j]:
                    return -1
                elif d[i][j] == d[i][k] + d[k][j]:
                    blist[i][j] = 0
    return sum([sum(l) for l in blist])//2

alist = []
blist = []
for i in range(n):
    a = list(map(int,input().split()))
    alist.append(copy.copy(a))
    blist.append(copy.copy(a))


ans = warshall_floyd(alist)
print(ans)