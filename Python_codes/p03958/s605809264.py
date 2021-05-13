# https://atcoder.jp/contests/code-festival-2016-qualc/tasks/codefestival_2016_qualC_b

k, t = map(int, input().split())
nums = [int(i) for i in input().split()]
MAX = max(nums)

ans = max(MAX - 1 - (k - MAX), 0)
print(ans)