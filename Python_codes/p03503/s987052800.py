MAX_TIME = 10
n = int(input().rstrip())
#２進法を
P = [sum(int(i) << MAX_TIME-k-1 for k, i in enumerate(input().rstrip().split())) for j in range(n)]
S = [list(map(int, input().rstrip().split())) for i in range(n)]
#予め2進数をカウントしておく
    # 予めビットをカウントしておく
pattern = [sum(i >> j & 1 for j in range(MAX_TIME)) for i in range(2 ** MAX_TIME)]
result = -float('inf')


for i in range(1, 2**MAX_TIME):
    temp = 0
    for l, j in zip(P, S):
        temp += j[pattern[l & i]]
    result = max(result, temp)
print(result)