#133_E
import sys
sys.setrecursionlimit(100000)
mod = 10 ** 9 + 7
n, k = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)
    
def dfs(frm, cur):
    if frm == -1:
        color_num = k - 1
    else:
        color_num = k - 2
        
    if k < len(edges[cur]):
        return 0
    
    mul = 1
    for to in edges[cur]:
        if to == frm:
            continue
        mul *= color_num
        mul %= mod
        color_num -= 1
        
    for to in edges[cur]:
        if to == frm:
            continue
        mul *= dfs(cur, to)
        mul %= mod
    
    return mul

print(k * dfs(-1, 0) % mod)