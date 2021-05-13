import math

N, K = list(map(lambda k: int(k), input().split(" ")))

# dice -> n
# n * 2^x >= K
# 2^x >= K / n
# x >= log2 (K / n)

p = [1 * (1/2) ** max([math.ceil(math.log2(K/(i + 1))), 0]) for i in range(N)]
print(sum(p)/N)