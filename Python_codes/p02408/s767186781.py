#トランプカード出力テスト
n = int(input())
my_card = [input() for i in range(n)]
card_list = ['S','H', 'C', 'D']
for suit in card_list:
    for num in range(1,14):
        card_check = suit+" "+str(num)
        if not(card_check in my_card):
            print(card_check)
