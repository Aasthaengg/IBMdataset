from sys import stdin, setrecursionlimit as srl
from threading import stack_size
srl(int(1e9)+7)
stack_size(int(1e8))

prime = 10**9 + 7

def get(i, j, m, value):
    if i==h-1 and j==w-1:
        return 1
    if value[i][j]!=-1:
        return value[i][j]
    ans = 0
    if i < h-1 and m[i+1][j]=='.':
        value[i+1][j] = get(i+1, j, m, value)
        ans += value[i+1][j]
    if j < w-1 and m[i][j+1]=='.':
        value[i][j+1] = get(i, j+1, m, value)
        ans += value[i][j+1]
    return ans%prime

h, w = map(int,input().split())
m = []
for i in range(h):
    m.append(input())
value = [[-1 for i in range(w)] for j in range(h)]
ans = get(0, 0, m, value)
print(ans)