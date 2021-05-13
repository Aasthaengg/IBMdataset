n, q = map(int, input().split())
que = []
for _ in range(n):
    p, t = input().split()
    que.append([p, int(t)])

now = 0
while len(que) != 0:
    if que[0][1] > q:
        que[0][1] -= q
        now += q
        que.append(que.pop(0))
    else:
        now += que[0][1]
        print("{} {}".format(que[0][0], now))
        que.pop(0)