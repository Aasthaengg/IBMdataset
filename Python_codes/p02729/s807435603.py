# The Number of Even Pairs
import math
N, M = map(int, input().split())

def combinations_count(N, M):
    return (math.factorial(N + M) // (math.factorial(N + M - 2) * math.factorial(2)))

ans = combinations_count(N, M) - N * M
print(ans)