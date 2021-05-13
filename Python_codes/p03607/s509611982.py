from collections import Counter
N = int(input())
A = [int(input()) for _ in range(N)]
C = Counter(A)
ans = sum(C[key] % 2 for key in C)
print(ans)