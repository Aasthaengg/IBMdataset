N = int(input())#配列の数を
h = list(map(int, input().split()))

dp = []
dp.append(0)#配列の先頭に0をk加える
dp.append(abs(h[1]-h[0]))#配列の2番目の値も固定なので　加えておく

for i in range(2,N):
     t1 = dp[i - 2] + abs(h[i] - h[i - 2])
     t2 = dp[i - 1] + abs(h[i] - h[i - 1])
     dp.append(min(t1, t2))#大小比較を行う



print(dp[-1])#配列の末尾の値を出力する