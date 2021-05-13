# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_A
# Result:
import sys

nums_len = int(sys.stdin.readline())
nums_str = sys.stdin.readline().split(' ')
nums = map(int, nums_str)

swap_count = 0
flag = True
while flag:
    flag = False
    for i in reversed(range(1, nums_len)):
        if nums[i] < nums[i - 1]:
            v = nums[i]
            nums[i] = nums[i - 1]
            nums[i - 1] = v
            swap_count += 1
            flag = True

print ' '.join(map(str, nums))
print swap_count