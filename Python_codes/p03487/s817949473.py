from collections import Counter
n = int(input())
A = Counter(map(int, input().split()))
ans = 0
for k, v in A.items():
    if k > v:
        ans += v
    elif k < v:
        ans += v - k

print(ans)
