# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_B
# Selection Sort
# Result:
import sys

nums_len = int(sys.stdin.readline())
nums_str = sys.stdin.readline().split(' ')
nums = map(int, nums_str)

swap_count = 0
for i in range(0, nums_len):
    minj = i
    for j in range(i, nums_len):
        if nums[j] < nums[minj]:
            minj = j
    if minj != i:
        v = nums[i]
        nums[i] = nums[minj]
        nums[minj] = v
        swap_count += 1

print ' '.join(map(str, nums))
print swap_count