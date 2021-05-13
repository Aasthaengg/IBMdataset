from collections import Counter
n, m = map(int, input().split())
a = list(map(int, input().split()))
s = [0] * (n+1)
for i in range(n): s[i+1] = s[i] + a[i]
s = [x % m for x in s]
ans = 0
for x in Counter(s).values():
    ans += x * (x-1) // 2
print(ans)