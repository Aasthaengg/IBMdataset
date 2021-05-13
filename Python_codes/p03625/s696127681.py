from collections import Counter

n = int(input())
A = list(map(int, input().split()))

C = Counter(A)
C = [[k, v] for k, v in C.items() if v >= 2]
C.sort(key=lambda x:x[0], reverse=True)

ans = 0
if len(C) >= 1:
    if C[0][1] >= 4:
        ans = C[0][0] * C[0][0]
    elif len(C) >= 2:
        ans = C[0][0] * C[1][0]

print(ans)