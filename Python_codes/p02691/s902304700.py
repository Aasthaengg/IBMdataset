N = int(input())
A = list(map(int, input().split()))
A = [0] + A

from collections import Counter

L1 = [i+a for i, a in enumerate(A)][1:]
L2 = [i-a for i, a in enumerate(A)][1:]

C1 = Counter(L1)
C2 = Counter(L2)
C = Counter(L1+L2)

ans = 0
for k in C.keys():
    ans += C1[k]*C2[k]
print(ans)