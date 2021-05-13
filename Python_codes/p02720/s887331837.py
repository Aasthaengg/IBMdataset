k = int(input())
nums = set()


def rec(past: int, num: int):
    nums.add(num)
    if num > 10**10:
        return
    if past > 0:
        rec(past - 1, num * 10 + past - 1)
    rec(past, num * 10 + past)
    if past < 9:
        rec(past + 1, num * 10 + past + 1)


for i in range(1, 10):
    rec(i, i)
ans = sorted(nums)
print(ans[k - 1])