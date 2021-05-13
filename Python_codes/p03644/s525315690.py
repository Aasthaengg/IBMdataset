n = int(input())
max_cnt = 0
max_num = 1

#1からnまでの数を調べる
for i in range(1, n + 1):
    count = 0
    num = i
    #iが2で割りきれるまで割る
    while i % 2 == 0 :
        count += 1
        i = i//2
    
    #割り切れる回数を更新
    if max_cnt < count :
        max_cnt = count
        max_num = num

print(max_num)