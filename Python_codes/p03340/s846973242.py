N = int(input())
A = list(map(int, input().split()))

left = 0
right = 0
right_max = N                                           # 右端の上限値 (配列の index の上限は N-1 だが、半開区間なので右端の上限は N)
total = 0
xtotal = 0
res = 0
for left in range(right_max):
    while right < right_max and total + A[right] == total ^ A[right]:
        total += A[right]
        xtotal ^= A[right]
        right += 1
    res += right - left
    if right == left:
        right += 1
    else:
        total -= A[left]
        xtotal = A[left]^xtotal
print(res)