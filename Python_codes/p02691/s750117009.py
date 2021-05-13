from collections import defaultdict
N = int(input())
arr = list(map(int, input().split()))
d = defaultdict(int)
ans = 0
for i in range(N):
    if i-arr[i] >= 0:
        ans += d[i-arr[i]]
    d[i+arr[i]] += 1
print(ans)