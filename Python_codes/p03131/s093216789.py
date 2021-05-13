import math

K, A, B = map(int, input().split())
A2B = B - A

# 最初は1枚
ans = 1

# 1枚からはじめって1円に考案できるかどうか
if K >= A - 1:
    K -= (A - 1)  # A枚になるように叩く
    ans += (A - 1) # A枚持っている
else:
    ans += K # 1円にならないので全部叩く
    K = 0 # 残りは0

# 交換する価値がある (増える)
if A2B > 2:
    times = K // 2  # 残り回数のうち，A->円，円->Bの回数だけ交換できる
    ans += A2B * times  # 交換で増える分
    ans += K % 2  # 残りの枚数
else: # 増えない場合，残っている回数は叩いて増やせばいい
    ans += K

print(ans)