n = int(input())
b = list(map(int, input().split()))
res = []
for _ in range(n):
    idx = 0
    for i in range(len(b)):
        if b[i] == i + 1:
            idx = i + 1
    if idx == 0:
        print(-1)
        exit()
    res.append(idx)
    b.pop(idx-1)
res = res[::-1]
for i in range(n): print(res[i])