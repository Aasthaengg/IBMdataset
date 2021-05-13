from collections import Counter

A = input()
len_a = len(A)

ans = len_a * (len_a - 1) // 2 + 1
for i in Counter(A).values():
    ans -= i * (i - 1) // 2

print(ans)
