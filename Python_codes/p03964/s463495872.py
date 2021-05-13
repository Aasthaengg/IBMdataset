from math import ceil
N = int(input())
T, A = 1, 1
for k in range(N):
    t, a = map(int,input().split())
    b = max(T//t,A//a)
    if t*b < T or a*b < A:
        b += 1
    T, A = t*b, a*b
print(T+A)
