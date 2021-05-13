import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    S = input()

    # 1の個数と0の個数を交互に記録
    nums = []
    if S[0] == "0":
        nums.append(0)
    i = 0
    while i < n:
        j = i
        while j < n and S[j] == S[i]:
            j += 1
        nums.append(j - i)
        i = j
    nums.append(0) if S[-1] == "0" else None

    # 累積和
    sums = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        sums[i + 1] = sums[i] + nums[i]

    res = 0
    for left in range(0, len(sums), 2):
        right = left + k * 2 + 1
        if right >= len(sums):
            right = len(sums) - 1
        res = max(res, sums[right] - sums[left])

    print(res)


if __name__ == '__main__':
    resolve()
