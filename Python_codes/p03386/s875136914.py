import sys
input = sys.stdin.readline

A, B, K = map(int, input().split())

L = set()
for i in range(min(K, B-A+1)):
    L.add(A+i)
    L.add(B-i)
L = sorted(list(L))
for i in range(len(L)):
    print(L[i])
