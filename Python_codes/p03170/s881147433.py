import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**7)
n, stones = map(int, readline().split())
a = list(map(int,readline().split()))
dp = [-1]*stones
def can_or_cant(rem, chance):
    if rem == 0:
        return True
    if dp[rem] != -1:
        return dp[rem]
    den = 2 if chance == 1 else 2
    for j in range(len(a)):
        if rem - a[j] >= 0 and can_or_cant(rem-a[j], den):
            dp[rem] = False
            return False
    dp[rem] = True
    return True


res = False
for i in range(n):
    if can_or_cant(stones - a[i], 1):
        res = True
        break
print("First" if res else "Second")

