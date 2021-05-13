import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,K = list(map(int, input().split()))
from collections import defaultdict
current = []
nums = defaultdict(int)
td = [None]*n
for i in range(n):
    t,d = list(map(int, input().split()))
    td[i] = (d,t)
td.sort(reverse=True)
ans = 0
for i in range(K):
    d,t = td[i]
    current.append((d, t))
    ans += d
    nums[t] += 1
j = K-1
total = len(nums)
ans += total**2
cur = ans
for i in range(K, n):
#     print(ans)
    d,t = td[i]
    if t not in nums:
        while j>=0 and nums[current[j][1]]<=1:
            j -= 1
        if nums[current[j][1]]>=2:
            nums[current[j][1]] -= 1
            nums[t] = 1
            cur -= current[j][0]
            cur += total*2+1 + d
            total += 1
            ans = max(ans, cur)
#             print(cur,j)
            j -= 1
print(ans)