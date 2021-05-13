N = int(input())

# mod = 1
# for n in range(N, 0, -1):
#     mod *= n

g = {}
for idx in range(N):
    x, y = map(int,input().split())
    g[idx] = (x, y)

ans = []
def dfs(curr, d):
    if len(seen) == N:
        ans.append(d)
        return
    
    for i in range(N):
        if i not in seen:
            seen.add(i)
            dis = ((g[curr][0] - g[i][0])**2 + (g[curr][1] - g[i][1])**2)**(1/2)
            dfs(i, d + dis)
            seen.discard(i)
    return    

for i in range(N):
    seen = set([i])
    dfs(i, 0)

ret = 0
for a in ans:
    ret += a
print(ret / len(ans))

