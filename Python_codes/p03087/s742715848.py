# https://atcoder.jp/contests/abc122/tasks/abc122_c

n, q = map(int, input().split())
s = input()

question = []
for _ in range(q):
    l, r = map(int, input().split())
    question.append((l - 1, r - 1))

nums = [0] * n
for i in range(1, n):
    if s[i - 1] == 'A' and s[i] == 'C':
        nums[i] = 1

for i in range(n - 1):
    nums[i + 1] += nums[i]

for l, r in question:
    ans = nums[r] - nums[l]
    print(ans)