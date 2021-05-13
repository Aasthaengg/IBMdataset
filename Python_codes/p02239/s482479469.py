import collections

N = int(input())
route = []
for i in range(N):
    a = list(map(int, input().split()))
    route.append(a[2:])
ans = [-1 for _ in range(N)]
ans[0] = 0
check = collections.deque([0])#now distance
while check:
    now = check.popleft()
    for next in route[now]:
        next -= 1
        if ans[next] == -1:
            check.append(next)
            ans[next] = ans[now]+1
for i in range(N):
    print(i+1, ans[i])

