from collections import Counter
n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))
d = Counter(sorted(d))
cnt = 0
for i in range(m):
    if t[i] in d and d[t[i]] > 0:
        d[t[i]] -= 1
        cnt += 1
    else: break
print("YES" if cnt == m else "NO")