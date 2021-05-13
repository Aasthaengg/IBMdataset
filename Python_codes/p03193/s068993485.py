n, h, w = [int(i) for i in input().split()]
ita = [[int(i) for i in input().split()] for i in range(n)]
ans = 0

for i in range(n):
    if ita[i][0] >= h and ita[i][1] >= w:
        ans += 1
print(ans)