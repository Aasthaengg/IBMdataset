import sys

n,k = map(int,input().split())
s = input()

# zero[i] = [左からi番目連続した0の数, 左の連続した1の数,右の連続した1の数]
# s=00010 の時、zero=[[3, 0, 1], [1, 1, 0]]
zero = []
string = s[0]
count = 0; left = 0; right = 0; num = 0
for i in range(n):
	if s[i] == string:
		count += 1
	else:
		if string == '0':
			num = count
			string = '1'
		else:
			if num != 0:
				zero.append([num,left,count])
			string = '0'
			left = count
			num = 1
		count = 1

# 右端の数字が0か1かで処理が変わる
if string == '0':
	zero.append([count,left,0])
else:
	zero.append([num,left,count])

# kが十分に大きければ全員逆立ちする
if len(zero) <= k:
	print(len(s))
	sys.exit()

# 左からk個の連続した0を全て1にしたときの、
# 連続した1の個数をresに格納
res = 0
for i in range(k):
	res += zero[i][0] + zero[i][1]
res += zero[i][2]

# 左端を削除し、右端に1つ追加する
# 多分しゃくとり法
ans = res
for i in range(len(zero)-k):
	res -= zero[i][0] + zero[i][1]
	res += zero[i+k][0] + zero[i+k][2]
	ans = max(ans,res)

print(ans)
