# 数値の取得
N = int(input())

# 1~9の積で表現できるか検査
cnt = 1
judge = ("No")
for cnt in range(1,10,1):
    if N // cnt <10\
    and N % cnt == 0:
        judge = ("Yes")
        break

# 結果を出力
print(judge)