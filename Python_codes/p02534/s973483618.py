# Kを受け取る
K = int(input())

# 文字列ACLを作るために、リストlを用意
l = ['A', 'C', 'L']

# 入力されたKの値に応じて、出力する文字列の分岐を作る
if 1<= K <= 5:
    K_letters = K*l
    out_letters = ''.join(K_letters)
    print(out_letters)

else:
    print('error')