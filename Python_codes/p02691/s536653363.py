from collections import Counter
N = int(input())
A = list(map(int, input().split()))
L = Counter(list(i + 1 + A[i] for i in range(N)))
R = Counter(list(j + 1 - A[j] for j in range(N)))
# print(L, R)
ans = 0
for k, v in R.items():
    ans += L[k] *  v
print(ans)
