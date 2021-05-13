from collections import defaultdict
n = int(input())
a = [list(map(int,input().split())) for i in range(n)]
dic = defaultdict(lambda :0)
cut = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:continue
            temp = a[i][k] + a[k][j]

            if a[i][j] > temp:
                print(-1)
                exit()

            if temp == a[i][j] and i < j and k != i and k != j:
                if not dic[(i, j)]:
                    cut += a[i][j]
                    dic[(i, j)] = 1
rec = 0
for i in range(n):
    for j in range(n):
        if i < j :rec += a[i][j]

print(rec - cut)