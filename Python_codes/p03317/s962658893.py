N, K = map(int, input().split())
A = list(map(int, input().split()))

# 1の場所を探す
pos = A.index(1)

count = 0
num_forward = pos  # 前方の残り数
num_backward = N - pos - 1  # 後方の残り数

# 前方にX回試行したときに負の余りが生じる場合は後方に回す
rest = num_forward % -(K - 1)
num_backward += rest

while num_forward > 0:  # 先頭まで1にする
    num_forward -= K - 1
    count += 1
while num_backward > 0:  # 末尾まで1にする
    num_backward -= K - 1
    count += 1
print(count)
