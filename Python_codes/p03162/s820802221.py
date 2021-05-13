N = int(input())

happy = [[0, 0, 0] for _ in range(N)]

happy[0] = [int(x) for x in input().split()]

for i in range(1, N):
    a, b, c = [int(x) for x in input().split()]
    happy[i][0] = max(happy[i - 1][1] + a, happy[i - 1][2] + a)
    happy[i][1] = max(happy[i - 1][2] + b, happy[i - 1][0] + b)
    happy[i][2] = max(happy[i - 1][0] + c, happy[i - 1][1] + c)

ans = max(happy[N - 1])

print(ans)