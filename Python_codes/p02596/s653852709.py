# coding: utf-8
# Your code here!

# 7で割り切れる数かを検証するということは1 ~ kで割ると良い
# ただし、毎回10をかけて7を足していると計算できない範囲まで大きくなるので毎回kで割ったあまりを用いる

k = int(input())

num = 7
if k == 1 or k == 7:
    print(1)
    exit()
for i in range(1, k + 1):
    num = num * 10 + 7
    if num % k == 0:
        print(i + 1)
        exit()
    else:
        num %= k
        
print(-1)
exit()
