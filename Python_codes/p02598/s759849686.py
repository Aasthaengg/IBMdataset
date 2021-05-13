import math

N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)

left = 1
right = A[0]
while int(left) != int(right):
    mid = (left + right) / 2
    k = sum(int(a / mid) if mid < a else 0 for a in A)
    if k <= K:
        if right == mid:
            break
        right = mid
    else:
        if left == mid:
            break
        left = mid
print(math.ceil(left))