# coding: utf-8
A, B, K = map(int, input().split())
a = set(i for i in range(A, min(A + K, B + 1)))
b = set(j for j in range(max(B - K + 1, A), B + 1))
c = list(a | b)
c.sort()
for k in c:
    print(k)
