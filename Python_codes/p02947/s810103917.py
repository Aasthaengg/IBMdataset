from collections import Counter

n = int(input())
w = [""] * n
for i in range(n):
    w[i] = list(input())
    w[i].sort()
    w[i] = "".join(w[i])

w = Counter(w)
ans = 0
for i in w.values():
    ans += i * (i - 1) // 2
print(ans)
