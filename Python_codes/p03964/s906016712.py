import math

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

x = l[0]
for i in range(1,n):
    #y = math.ceil(x[0] / l[i][0]) # 'ceil'では 'WA'.
    #z = math.ceil(x[1] / l[i][1]) # 'ceil'では、商が桁の大きなfloatの場合、高次桁で結果に狂いが生じる.
    y = -(-x[0] // l[i][0])
    z = -(-x[1] // l[i][1])
    x = [max(y, z) * j for j in l[i]]

print(sum(x))
