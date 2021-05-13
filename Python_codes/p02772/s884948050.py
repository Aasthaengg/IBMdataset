# 数値の取得
num_cnt = int(input())
num_list = list(map(int,input().split()))

# 数値の検査後メッセージを出力
judge = "APPROVED"
for cnt in range(0,num_cnt,1):
    if num_list[cnt] % 2 == 0\
    and num_list[cnt] % 3 != 0\
    and num_list[cnt] % 5 != 0:
      judge = "DENIED"
      
print(judge)