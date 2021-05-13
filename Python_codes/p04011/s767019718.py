# 044a

N = int(input())    # 宿泊数Nを代入
K = int(input())    # 最初のK泊を代入
X = int(input())    # K泊までの一泊あたりの料金Xを代入
Y = int(input())    # K+1泊目以降の一泊あたりの料金Yを代入

if N <= K:
    hotel_fee = N * X
else:
    hotel_fee = K * X + (N - K) * Y

print(hotel_fee)

