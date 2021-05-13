graph = [[-1 for _ in range(15)] for _ in range(15)]
n = int(input())
for index in range(n):
    a = int(input())
    for _ in range(a):
        x, y = map(int, input().split())
        graph[index][x-1] = y

answer = 0
for index in range(2 ** n):
    honests = [0 for _ in range(n)]
    for shift in range(n):
        if (index >> shift) & 1:
            honests[shift] = 1
    ok = True
    for idx1 in range(n):
        if honests[idx1]:
            for idx2 in range(n):
                if graph[idx1][idx2] == -1:
                    continue
                if graph[idx1][idx2] != honests[idx2]:
                    ok = False
    if ok:
        answer = max(answer, honests.count(1))

print(answer)