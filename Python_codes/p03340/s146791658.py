N = int(input())
A = tuple(map(int, input().split()))

right = left = 0
xor_sum = 0
total = 0
while right < N:
    if xor_sum ^ A[right] == xor_sum + A[right]:
        xor_sum += A[right]
        right += 1
        total += right - left
    elif right == left:
        right += 1
        left += 1
    else:
        xor_sum -= A[left]
        left += 1
print(total)
