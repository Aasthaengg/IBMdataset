import sys
sys.setrecursionlimit(3000)

n = int(input())
X = []
for _ in range(n):
    x = list(map(int, input().split()))
    if x[1] != 0:
        X.append(x[2:])
    else:
        X.append([])

df = [[0, 0] for _ in range(n)]
t = 0
def search(i = 0):
    global t
    if df[i][0] == 0:
        t += 1
        df[i][0] = t
    for x in X[i]:
        if df[x - 1][0] == 0:
            search(x - 1)
    if df[i][1] == 0:
        t += 1
        df[i][1] = t

for i in range(n):
    search(i)

for i, x in enumerate(df):
    print('{} {} {}'.format(i + 1, x[0], x[1]))
