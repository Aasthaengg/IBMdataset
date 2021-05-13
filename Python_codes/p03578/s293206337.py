from collections import Counter
n = int(input())
d = Counter(list(map(int, input().split())))
m = int(input())
T = list(map(int, input().split()))

ans = "YES"
for t in T:
    if t in d and d[t] > 0:
        d[t] -= 1
    else:
        ans = "NO"
        break
print(ans)