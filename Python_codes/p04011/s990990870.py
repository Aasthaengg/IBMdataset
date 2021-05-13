# A - 高橋君とホテルイージー
# https://atcoder.jp/contests/abc044/tasks/abc044_a

N = int(input())
K = int(input())
X = int(input())
Y = int(input())

result = 0

for i in range(N):
    if i < K:
        result += X
    else:
        result += Y

print(result)
