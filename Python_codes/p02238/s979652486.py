n = int(input())
V = [[] for _ in range(n)]
for i in range(n):
    data = list(map(int, input().split(" ")))
    V[i] = data[2:]

answer = [[None, None] for _ in range(n)]

counter = 1


def dfs(v):
    global counter
    if answer[v][0] == None:
        answer[v][0] = counter
        counter += 1
        # ノードの子供の管理
        for e in V[v]:
            dfs(e-1)
        answer[v][1] = counter
        counter += 1


for i in range(len(answer)):
    if answer[i][0] == None:
        dfs(i)

for i in range(len(answer)):
    print(str(i+1) + " " + " ".join(map(str, answer[i])))

