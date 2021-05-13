from collections import Counter
A = input()
n = len(A)
C = Counter(A)

dup = 0
for k, cnt in C.items():
    dup += (cnt * (cnt-1)//2)

ans = n * (n-1) // 2 - dup + 1

print(ans)