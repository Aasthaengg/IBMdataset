#n = 候補の数
n = int(input())
#t - h[i] * 0.006
#a = 基準温度
t,a = map(int,input().split())
h = list(map(int,input().split()))
#o = 計算結果格納
o = []

for i in range(n):
    o.append(t - h[i] * 0.006)

#p = 基準温度に最も近い場所の差
p = abs(a - o[0])
#q = 基準地点の番号
q = 0
for i in range(n)[1:]:
    if abs(a - o[i]) < p:
        p = abs(a - o[i])
        q = i

print(q + 1)