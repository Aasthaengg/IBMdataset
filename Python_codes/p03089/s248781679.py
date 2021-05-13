# https://atcoder.jp/contests/agc032/tasks/agc032_a
import sys

n = int(input())
nums = [int(i) - 1 for i in input().split()]
ans = []
for i in range(n):
    for j in range(len(nums) - 1, -1, -1):
        if nums[j] == j:
            ans.append(j + 1)
            del nums[j]
            break
    else:
        print(-1)
        sys.exit()
for a in ans[::-1]:
    print(a)
