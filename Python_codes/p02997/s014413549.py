import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7

N, K = map(int, input().split())

G = []
G_append = G.append
for i in range(2, N + 1):
    G_append([1, i])

NOW = (N - 1) * (N - 2) // 2

if K > NOW:
    print (-1)
    exit()

flag = True
for i in range(2, N):
    for j in range(i + 1, N + 1):
        if K < NOW:
            G.append([i, j])
            NOW -= 1
        else:
            flag = False
            break
    if not flag:
        break

print (len(G))
for tmp in G:
    print (*tmp, sep = ' ')
