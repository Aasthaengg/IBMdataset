import sys
input = sys.stdin.readline
n, m = map(int, input().split())
q = [list(map(int, input().split())) for i in range(m)]

g = [[] for i in range(n+1)]

for i in range(m):
    a, b, c = q[i]
    g[a].append((b, c))
    g[b].append((a, -c))

people = [-10**10] * (n+1)

flag = 1
for i in range(1, n+1):
    if people[i] != -10**10:
        continue
    q = [i]
    people[i] = 0
    while q:
        now = q.pop()
        for next, dist in g[now]:
            if people[next] == -10**10:
                q.append(next)
                people[next] = people[now] + dist
            else:
                if people[next] == people[now] + dist:
                    continue
                else:
                    flag = 0
                    break
        if flag == 0:
            break

if max(people[1:]) - min(people[1:]) > 10**9:
    flag = 0

if flag == 1:
    print("Yes")
else:
    print("No")
