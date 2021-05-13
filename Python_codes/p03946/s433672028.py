N, T = map(int, input().split())
A = list(map(int, input().split()))

# 最大収益
max_income = 0
# リンゴの最低価格
min_num = A[0]
# 青木君が減らさないといけない組の数
comb = 0
    
# 2つ目の町から探索
# n = 現在の町のリンゴの価格
for n in A[1:]:
    # 最低価格を更新する
    if n < min_num:
        min_num = n
    
    # 最大利益を更新する
    elif n - min_num > max_income:
        max_income = n-min_num
        # 組数を1にする
        comb =1
    
    # 最大利益を持つ組が2個あった場合、
    elif n - min_num == max_income:
        # 組数を1増やす
        comb +=1
        

print(comb)