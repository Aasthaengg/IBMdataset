# https://atcoder.jp/contests/code-festival-2016-quala/tasks/codefestival_2016_qualA_b

n = int(input())
nums = [int(i) for i in input().split()]

ans = 0
d = set()
for i in range(n):
    a = i + 1
    b = nums[i]
    if (a, b) in d or (b, a) in d:
        ans += 1
    else:
        d.add((a, b))
        d.add((b, a))
print(ans)
