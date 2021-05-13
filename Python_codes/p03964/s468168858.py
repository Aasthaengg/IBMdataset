N = int(input())
ta = [list(map(int, input().split())) for _ in range(N)]
t = 1
a = 1
for i in range(N):
    if t % ta[i][0] != 0:
        ttmp = t // ta[i][0] + 1
    else:
        ttmp = t // ta[i][0]

    if a % ta[i][1] != 0:
        atmp = a // ta[i][1] + 1
    else:
        atmp = a // ta[i][1]
    n = max(ttmp, atmp)
    t = (n * ta[i][0])
    a = (n * ta[i][1])

print(t + a)