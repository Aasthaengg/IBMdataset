from collections import deque

N = int(input())
tree = [[] for i in range(N)]

for _ in range(N):
    tmp = list(map(int, input().split()))
    for i in range(2, len(tmp)):
        tree[tmp[0]-1].append(tmp[i]-1)

q = deque(tree[0])
cnt = deque([1]*len(tree[0]))
s = {}
ans = [-1]*N

ans[0] = 0
s[0] = True
while len(q) != 0:
    g = q.popleft()
    c = cnt.popleft()
    if ans[g] == -1:
        ans[g] = c
        s[g] = True

    for tmp in tree[g]:
        if not(tmp in s):
            q.append(tmp)
            cnt.append(c+1)

for i in range(N):
    print(i+1, ans[i])

