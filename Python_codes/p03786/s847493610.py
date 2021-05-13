from itertools import accumulate
n = int(input())
a = list(map(int, input().split()))
a.sort()
asum = list(accumulate(a))

ans = 0
for i in range(n-1):
  if asum[i]*2>=a[i+1]:
    ans += 1
  else:
    ans = 0
print(ans+1)