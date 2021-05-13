# Nを定義
N = int(input())

# Nを３で割った時のあまりを出す
Surplus =  int( N ) % 3

# 条件分岐
if Surplus < 3:
    print( N //3 )