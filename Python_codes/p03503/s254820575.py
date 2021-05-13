n = int(input())
f = [list(map(int, input().split())) for _ in range(n)]
p = [list(map(int, input().split())) for _ in range(n)]

ans = []
stk = [[0] * n]

for i in range(10):
    for j in range(len(stk)):
        total = 0
        arr = []
        for k in range(n):
            open_shops = stk[j][k] + f[k][i]
            arr.append(open_shops)
            total += p[k][open_shops]
        ans.append(total)
        stk.append(arr)

print(max(ans))