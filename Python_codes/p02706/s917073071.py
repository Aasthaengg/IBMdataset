
getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]
 
n, m = getList()
nums = getList()
sn = sum(nums)
if sn > n:
  print(-1)
else:
  print(n - sn)