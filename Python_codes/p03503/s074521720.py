n = int(input())
op = []
for _ in range(n):
    l = list(map(int, input().split()))
    op.append(l)
score = []
for _ in range(n):
    l = list(map(int, input().split()))
    score.append(l)
final = -999999999999999999999999


for pat in range(1,2**10):
    openNum = [0] * n
    for i in range(10):
        if ((pat >> i) & 1) == 1:
            for j in range(n):
                if op[j][i] == 1:
                    openNum[j] += 1
    res = 0
    for i in range(n):
        res += score[i][openNum[i]]
    final = max(final, res)
print(final)
