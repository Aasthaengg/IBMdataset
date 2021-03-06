# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_e
n = int(input())
nums = map(int, input().split())
MOD = 1000000007
ans = 1
cnt = [3 if i == 0 else 0 for i in range(n + 1)]

for num in nums:
    ans = ans * cnt[num] % MOD
    if ans == 0:
        break
    cnt[num] -= 1
    cnt[num+1] += 1

print(ans)
