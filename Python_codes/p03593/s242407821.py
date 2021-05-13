from collections import Counter
H, W = map(int, input().split())

S = ""
for _ in range(H):
    S += input()

# print(S)
character_counter = Counter(S)
# print(character_counter)
g1 = (H % 2) * (W % 2)  # 行と列のどちらかが偶数であれば0
g2 = (W // 2) * (H % 2) + (H // 2) * (W % 2)  # 奇数のときに2つのブロックのペアをもてる
g4 = (H // 2) * (W // 2)
# 
# print(g1*1+g2*2+g4*4)  # この値を使い切る必要がある
# print(g1)
# print(g2)
# print(g4)
# print(character_counter)

character_counter_list = sorted(list(character_counter.values()), reverse=True)
# print(character_counter_list)

# g1を使う
for i in range(len(character_counter_list)):
    if character_counter_list[i] % 2 == 1 and g1 > 0:
        character_counter_list[i] -= 1
        g1 -= 1

# g2を使う
for i in range(len(character_counter_list)):
    if character_counter_list[i] % 4 == 2 and g2 > 0:
        character_counter_list[i] -= 2  # これによってmod4で0になっている
        g2 -= 1

if g2 % 2 == 1:  # g2が奇数個余っていたら終わり
    print("No")
    exit()

# 余ったg2は2つで1個分のg4として使える
g4 += (g2//2)
g2 = 0
# g4を使う
for i in range(len(character_counter_list)):
    if character_counter_list[i] % 4 == 0 and g4 > 0:
        tmp = (character_counter_list[i] // 4)
        character_counter_list[i] -= (4*tmp)  # もし文字の数が8個とかなら、g4を2つ使える
        g4 -= tmp
# print(character_counter_list)
# print(g1)
# print(g2)
# print(g4)

if g1 == 0 and g2 == 0 and g4 == 0 and sum(character_counter_list) == 0:  # 無事に使い切れたらYes
    print('Yes')
else:
    print('No')
