N, P = map(int, input().split())
A = list(map(int, input().split()))

# 奇数の数を数える
odd_cnt = 0
for a in A:
    if a % 2 != 0:
        odd_cnt += 1

# 全てのが偶数の時
if odd_cnt == 0:
    if P == 0:
        print(2**N)
    else:
        print(0)
    exit(0)

print(2**(N-1))
