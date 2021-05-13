# 日立製作所 社会システム事業部 プログラミングコンテスト2020: B – Nice Shopping
A, B, M = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(j) for j in input().split()]
x, y, c = [], [], []
for k in range(M):
    tmp = [int(i) for i in input().split()]
    x.append(tmp[0])
    y.append(tmp[1])
    c.append(tmp[2])

prices = []

prices.append(min(a) + min(b))

for k in range(M):
    prices.append(a[x[k] - 1] + b[y[k] - 1] - c[k])

print(min(prices))