from collections import Counter
n = int(input())
a = [int(input()) for i in range(n)]
p = Counter(a)
ans = 0
for i in p:
    if p[i] % 2 == 1:
        ans += 1
print(ans)
