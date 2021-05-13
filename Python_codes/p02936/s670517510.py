import sys, collections
input = sys.stdin.readline

n, q = map(int, input().split())
graph = [[] for i in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
add = [0 for i in range(n + 1)]
for i in range(q):
    p, x = map(int, input().split())
    add[p] += x
flag = [False for i in range(n + 1)]
check = collections.deque([1])
while check:
    test = check.popleft()
    flag[test] = True
    num_list = graph[test]
    for i in num_list:
        if flag[i] == True:
            pass
        else:
            add[i] += add[test]
            check.append(i)
for i in range(n):
    print(add[i + 1], end = " ")
print()