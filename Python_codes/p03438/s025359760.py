import math
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

operation_num = sum(b) - sum(a)
x = 0 # 操作回数
y = 0
z = 0
for i in range(n):
    x += b[i]-a[i]
    y += max(a[i]-b[i], 0)
    z += max(math.ceil((b[i]-a[i])/2), 0)
# print(x, y)
if x - y < 0 or x - z < 0:
    print('No')
else:
    print('Yes')
