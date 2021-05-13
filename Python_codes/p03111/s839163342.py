n, a, b, c = map(int, input().split())

target = [a, b, c]
l = [int(input()) for _ in range(n)]

ans = 10**9

for i in range(1, 4 ** n):
    q = bin(i)[2:].zfill(n * 2)
    pattern = [q[2 * j:2 * j + 2] for j in range(n)]
    k = [[], [], []]
    for j in range(n):
        t = int(pattern[j], 2)
        if t == 0:
            continue
        k[t-1].append(l[j])
    if len(k[0]) * len(k[1]) * len(k[2]) == 0:
        continue
    cost = 0
    for j in range(3):
        cost += abs(sum(k[j]) - target[j]) + (len(k[j]) - 1) * 10
    ans = min(cost, ans)

print(ans)
