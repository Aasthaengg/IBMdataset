N, C = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]

ans, value = 0, 0
for i in L:
    cost = i[0]
    value += i[1]
    ans = max(ans, value - cost)

value = 0
for i in L[::-1]:
    cost = C - i[0]
    value += i[1]
    ans = max(ans, value - cost)

rList = [0] * (N + 1)
value = 0
for i in range(N):
    sushi = L[i]
    cost = sushi[0]
    value += sushi[1]
    rList[i + 1] = max(rList[i], value - cost)

lList = [0] * (N + 1)
value = 0
for i in range(N):
    sushi = L[-1-i]
    cost = C - sushi[0]
    value += sushi[1]
    lList[i + 1] = max(lList[i], value - cost)

value = 0
for i in range(N):
    sushi = L[i]
    cost = sushi[0]
    value += sushi[1]
    ans = max(ans, value - cost * 2 + lList[N - (i + 1)])

value = 0
for i in range(N):
    sushi = L[-1-i]
    cost = C - sushi[0]
    value += sushi[1]
    ans = max(ans, value - cost * 2 + rList[N - (i + 1)])

print(ans)