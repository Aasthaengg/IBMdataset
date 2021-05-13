import math
N, K = map(int, input().split())
A = list(map(int, input().split()))
A_min = min(A)
index = A.index(A_min)
ans = 0
left = index
right = N - 1 - index
if left % (K - 1) != 0:
    right -= K - 1 - left % (K - 1)
elif right % (K - 1) != 0:
    left -= K - 1 - right % (K - 1)
ans += math.ceil(left / (K - 1))
ans += math.ceil(right / (K - 1))   
print(ans)