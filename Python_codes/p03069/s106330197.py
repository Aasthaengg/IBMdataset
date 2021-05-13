n = int(input())
s = list(input())

l = [[0, 0] for i in range(n + 1)]
for i in range(n):
    preB, preW = l[i]
    if s[i] == '#':
        l[i + 1] = [preB + 1, preW]
    else:
        l[i + 1] = [preB, preW + 1]

SUM_W = l[-1][1]
ans = 10 ** 10
for i, j in l:
    temp = i + SUM_W - j
    if temp < ans:ans = temp
print(ans)