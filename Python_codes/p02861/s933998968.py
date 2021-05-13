import itertools

N = int(input())
data = [[int(e) for e in input().split(" ")] for _ in range(N)]

ans = 0
cnt = 0
for path in itertools.permutations([i for i in range(N)]):
    dis = 0
    cnt += 1
    for i in range(N - 1):
        u = path[i]
        v = path[i + 1]

        dis += ((data[u][0] - data[v][0]) ** 2 +
                (data[u][1] - data[v][1]) ** 2)**(1 / 2)

    ans += dis

ans /= cnt
print(ans)
