from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

ans = n
data = defaultdict(int)
for i in range(n):
    data[a[i]] += 1
    if data[a[i]] >= 2:
        ans -= 1
print(ans if ans % 2 == 1 else ans - 1)