import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n = int(input())
    nums = []
    n6 = 6
    while n6 <= n:
        nums.append(n6)
        n6 = n6 * 6
    n9 = 9
    while n9 <= n:
        nums.append(n9)
        n9 = n9 * 9
    nums.sort(reverse=True)
    dp = [i for i in range(2 * n + 1)]
    for num in nums:
        for j1 in range(n + 1):
            dp[j1+num] = min(dp[j1+num], dp[j1] + 1)
    print(dp[n])


if __name__ == '__main__':
    main()
