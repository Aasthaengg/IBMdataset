N = int(input())

ans = [0] * (N+1)   # 答え用のリストを用意する

for x in range(1,100):      # Nの上限が10**4なのでルート(10**4)までで計算
    for y in range(1,100):
        for z in range(1,100):
            a = x * x + y * y + z * z + x * y + y * z + z * x
            if a <= N:      # 条件より計算結果aはNを超えてはならない
                n = a       # 計算結果aがn（インデックス番号）となるように
                ans[n] += 1 #リストのn番目のインデックスでカウント
      
for n in range(1,N+1):
    print(ans[n])