# 2つの整数の取得
a,b = map(int,input().split())
 
# aもしくはbが偶数であるかをもとに結果を出力
if (a % 2) == 0 or (b % 2) == 0:
    print("Even")
else:
    print("Odd")