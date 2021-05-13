N = int(input())
K = int(input())
X = int(input())
Y = int(input())

sum_num = 0
for i in range(1, N + 1):
    if i > K:
        sum_num += Y
    else:
        sum_num += X

print(sum_num)
