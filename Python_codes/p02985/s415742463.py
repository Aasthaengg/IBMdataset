import sys
input = sys.stdin.readline

MOD = 10 ** 9 + 7

N, K = map(int, input().split())
g = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)


if N == 1 and K == 1:
    print (1)
    exit()

check = [0] * (N + 1)
count = [K - 1] * (N + 1)

check[1] = 1
# count[1] -= 1

ans = K
stack = [1]
while stack:
    tmp = stack.pop()
    for next_ in g[tmp]:
        if check[next_] == 1:
            continue
        ans *= count[tmp]
        ans %= MOD
        count[tmp] -= 1
        count[next_] -= 1
        stack.append(next_)
        check[tmp] = 1

print (ans)
