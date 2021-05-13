N, M = map(int, input().split())

e_IN = [[] for _ in range(N+1)]
e_OUT = [[] for _ in range(N+1)]

for _ in range(M):
    l, r, d = map(int, input().split())
    e_OUT[l].append((r, d))
    e_IN[r].append((l, d))

posx = [-1] * (N + 1)


def dfs(v):
    #　0<=x<=10**9に注意
    node = [v]
    posx[v] = 0
    diameter = 0
    while node:
        s = node.pop()
        ds = posx[s]
        for t, dt in e_OUT[s]:
            dist = ds + dt
            if posx[t] != -1:
                if posx[t] != dist:
                    return False
                else:
                    continue
            posx[t] = dist
            node.append(t)
            diameter = max(diameter, dist)
    if diameter <= 10 ** 9:
        return True
    else:
        return False


ans = "Yes"
for i in range(N + 1):
    if len(e_IN[i]) == 0:
        posx[i] = 0
        bl = dfs(i)
        if not bl:
            ans = "No"
            break

if - 1 in posx:
    ans = "No"

print(ans)
