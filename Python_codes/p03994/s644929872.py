import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    S = input()
    K = int(input())
    nums = []
    a = ord("a")
    for s in S:
        nums.append(ord(s) - a)

    for i in range(len(S)):
        if nums[i] == 0:
            continue
        diff = 26 - nums[i]
        if diff <= K:
            nums[i] = 0
            K -= diff

    if K > 0:
        nums[-1] = (nums[-1] + K) % 26

    ans = ""
    for n in nums:
        ans += chr(n + a)
    print(ans)


if __name__ == "__main__":
    main()
