n, k = map(int, input().split())
A = list(map(int, input().split()))

Amin = A.index(1)

left = len(A[:Amin])
right = len(A[Amin:])

ans = 0
if left <= right:
    ans += left // (k-1)
    right += left % (k-1)
    ans += ((right-1) + (k-2)) // (k-1)
else:
    ans += (right-1) // (k-1)
    left += right % (k-1)
    ans += (left + (k-2)) // (k-1)
print(ans)