N, M = map(int, input().split())

g_cards = list(map(int, input().split()))

# key-valueデータで管理
dict_cards = []
for card in g_cards:
	dict_cards.append([card, 1])

# 操作
for i in range(M):
	# sizeと同じ枚数のカードが増えたと考える
	size, val = map(int, input().split())
	dict_cards.append([val, size])

# 降順にする
s_dict_cards = sorted(dict_cards, key=lambda x: -x[0])

s_cards = []
for data in s_dict_cards:
	s_cards += [data[0]] * data[1]
	if(len(s_cards) >= N):
		break
# 出力
sum_val = sum(s_cards[:N])
print(sum_val)