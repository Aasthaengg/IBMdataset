N, M = map(int, input().split())                       # 区間の数

imos = [0]*(10**5+2)

for _ in range(M):
    a, b = map(int, input().split())    # 区間は閉区間 [a,b] で与えられる
    imos[a] += 1
    imos[b+1] -= 1                      # 半開区間を作るために b+1 としておく点に注意。区間を使った回数を聞かれた場合はまた変わるので注意。

res = [0]
for k in imos:
    res.append(res[-1] + k)

print(res.count(M))
