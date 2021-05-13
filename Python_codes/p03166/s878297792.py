from collections import defaultdict, deque
n, m = map(int, input().split())
outs = defaultdict(list)
rv = defaultdict(list)
ins = defaultdict(int)
for i in range(m):
    x, y = map(int, input().split())
    outs[x].append(y)
    rv[y].append(x)
    ins[y] += 1
q = deque(i for i in range(1, n + 1) if ins[i] == 0)
ans = []
while q:
    st = q.popleft()
    ans.append(st)
    for to in outs[st]:
        ins[to] -= 1
        if ins[to] == 0:
            q.append(to)

dp = [0] * (n + 1)
for value in ans:
    dp[value] += max([0]+[dp[i]+1 for i in rv[value]])
print(max(dp))