n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
m = 10**19
# 地点の番号(=1)
idx = 0
for i in range(n):
    # 平均気温
    d = t - h[i]*0.006
    # A度に最も近い地点
    if abs(a-d) < m:
        m = abs(a-d)
        idx = i+1
print(idx)
