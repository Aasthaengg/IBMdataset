import sys
def input():
    return sys.stdin.readline().strip()

n, m = map(int, input().split())
l, d = [[] for _ in range(n)], [[] for _ in range(n)]
for _ in range(m):
    i, j, k = map(int, input().split())
    i -= 1
    j -= 1
    l[i].append(j)
    l[j].append(i)
    d[i].append(k)
    d[j].append(-k)

# DFS
seen = ['yet' for _ in range(n)]
todo = []
for i in range(n):
    if seen[i] != 'yet':
        continue
    seen[i] = 0
    todo.append(i)
    while todo != []:
        j = todo.pop(-1)
        for k in range(len(l[j])):
            if seen[l[j][k]] != 'yet':
                if seen[j] + d[j][k] != seen[l[j][k]]:
                    print('No')
                    exit()
                continue
            seen[l[j][k]] = seen[j] + d[j][k]
            todo.append(l[j][k])
print('Yes')