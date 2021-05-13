#%%
n, k = map(int, input().split())
reach = [[] for _ in range(n)]
mod = 10**9 + 7
for i in range(n-1):
    a, b = map(lambda x: int(x)-1, input().split())
    reach[a].append(b)
    reach[b].append(a)

def kai(i, j, mod):
    tmp = 1
    for x in range(i, i-j, -1):
        tmp *= x
        tmp %= mod
    return tmp

def dfs(st, n, k, reach, mod):
    check = [0] * n
    stack = [st]
    ans = k
    check[st] = 1
    while len(stack) > 0:
        tmp = stack.pop(-1)
        tmp_list = reach[tmp]
        alredy = 1
        yet = 0
        for i in tmp_list:
            if check[i] != 1:
                stack.append(i)
                check[i] = 1
                yet += 1
            else:
                alredy += 1
        t = kai(k-alredy, yet, mod)
        ans *= t
        ans %= mod
    return ans

ans = dfs(0, n, k, reach, mod)
print(ans)