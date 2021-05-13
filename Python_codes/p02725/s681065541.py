k, n = map(int, input().split())
a = list(map(int, input().split()))

max_d = 0

for i in range(n):
    d = a[(i + 1) % n] - a[i] #隣接する2軒の距離の最大値を算出
    if d < 0: #n番目-1番目の場合
        d += k
    max_d = max(max_d, d)

print(k - max_d) #一周から最長の隣接距離を引く