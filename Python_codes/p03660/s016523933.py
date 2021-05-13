import collections

n = int(input())
graph = [[] for i in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
flag = [False for i in range(n + 1)]
flag2 = [False for i in range(n + 1)]
dis_f = [0 for i in range(n + 1)]
dis_s = [0 for i in range(n + 1)]
queue = collections.deque([1])
while queue:
    test = queue.popleft()
    flag[test] = True
    for i in graph[test]:
        if flag[i] == False:
            queue.append(i)
            dis_f[i] = dis_f[test] + 1
queue2 = collections.deque([n])
while queue2:
    test = queue2.popleft()
    flag2[test] = True
    for i in graph[test]:
        if flag2[i] == False:
            queue2.append(i)
            dis_s[i] = dis_s[test] + 1
count_f = 0
count_s = 0
for i in range(n):
    if dis_f[i + 1] <= dis_s[i + 1]:
        count_f += 1
    else:
        count_s += 1
if count_f > count_s:
    print("Fennec")
else:
    print("Snuke")