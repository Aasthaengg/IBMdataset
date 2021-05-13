import collections, sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
for i in range(m):
    l, r, d = map(int, input().split())
    graph[l].append([r, d])
    graph[r].append([l, -d])
place = [None for i in range(n + 1)]

num = 0
flag = True
while num <= n:
    if flag == False:
        break
    if place[num] != None:
        num += 1
        continue
    place[num] = 0
    queue = collections.deque([num])
    while queue:
        if flag == False:
            break
        test = queue.popleft()
        for i in graph[test]:
            if place[i[0]] != None:
                if place[i[0]] - place[test] != i[1]:
                    flag = False
                    break
            else:
                place[i[0]] = place[test] + i[1]
                queue.append(i[0])
    else:
        num += 1
if flag == True:
    print("Yes")
else:
    print("No")