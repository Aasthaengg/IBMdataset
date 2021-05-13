N = int(input())
link = [set() for i in range(N)]
for i in range(N-1):
    u, v, w = map(int,input().split())
    link[u-1] |= {(v-1,w)}
    link[v-1] |= {(u-1,w)}
check = [(0, 0, -1)]
ans = [-1 for i in range(N)]
while check:
    now, d, From = check.pop()
    ans[now] = d % 2
    for next, dist in link[now]:
        if next == From:
            continue
        else:
            check.append((next, d + dist, now))
print('\n'.join(map(str,ans)))