n, *a = map(int, open(0).read().split())
# 状態1: iとi+1が1違う
# 状態2: iとi+1が同じ
# これ以外のiとi+1の関係があったら構築できない

# 状態1ではi+1を作る過程でiも作れる。
# 状態2ではi+1を作った後にiを作る必要がある。
# 後ろから見てa[i] - 1 == a[i - 1]となってる数を数えなければおｋ

# check
if a[0] != 0:
	print(-1)
	exit()
for i in range(n - 1):
	if a[i + 1] - a[i] > 1:
		print(-1)
		exit()

# count
i = n - 1
ans = 0
while i > 0:
	ans += a[i]
	while i > 0 and a[i] - 1 == a[i - 1]:
		i -= 1
	i -= 1
print(ans)
