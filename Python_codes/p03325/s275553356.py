import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

L = []
for i in range(N):
    n = bin(A[i])[::-1].find('1')
    if n != 0:
        L.append(n)
if not L:
    print(0)
else:
    print(sum(L))
