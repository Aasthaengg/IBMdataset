n, m = map(int, input().split())
K = []
A = []
for i in range(n):
    L = list(map(int, input().split()))
    K.append(L[0])
    A.append(L[1:])
# print(A)
Aall = []
for e in A:
    Aall += e
# print(Aall)
ans = 0
for i in range(1, m + 1):
    if Aall.count(i) == n:
        ans += 1
print(ans)
