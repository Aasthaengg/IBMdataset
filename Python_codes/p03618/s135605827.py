from collections import Counter
a = input()
k = Counter(a).values()
ans = len(a) * (len(a) - 1) // 2
for k_v in k:
    if k_v > 1:
        ans -= k_v * (k_v - 1) // 2
print(ans + 1)