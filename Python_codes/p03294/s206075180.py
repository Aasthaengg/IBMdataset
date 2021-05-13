# 合計が最大になるのは、余りが各aにおいてa-1となるとき。
n = int(input())
a = list(map(int, input().split()))
# 各aから1ずつ引くをn繰り返しているため。
ans = sum(a) - n
print(ans)