#%%
n, m = map(int, input().split())
p = list(map(int, input().split()))
x, y = [0] * m, [0] * m
reach = [[] for _ in range(n + 1)]
for i in range(m):
    x[i], y[i] = map(int, input().split())
    reach[x[i]].append(y[i])
    reach[y[i]].append(x[i])


check = [0] * (n + 1)
color = [-1] * (n + 1)
c = -1

for i in range(n + 1):
    if check[i] == 1:
        pass
    else:
        c += 1
        check[i] = 1
        stack = reach[i]
        color[i] = c
        while len(stack) >= 1:
            tmp = stack.pop(-1)
            color[tmp] = c
            check[tmp] = 1
            tmp_list = reach[tmp]
            for i in range(len(tmp_list)):
                if check[tmp_list[i]] == 0:
                    stack.append(tmp_list[i])
                    check[tmp_list[i]] = 1
                else:
                    pass

color.pop(0)
#print(color)

ans_list = [0] * n
for i in range(n):
    ans_list[i] = color[p[i] - 1]
#print(ans_list)

ans = 0
for i in range(n):
    if color[i] == ans_list[i]:
        ans += 1
print(ans)