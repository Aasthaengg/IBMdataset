import sys
input = sys.stdin.buffer.readline
N = int(input())

L = [-1] * 100
L[0] = 2
L[1] = 1
for i in range(2, 100):
    L[i] = L[i - 1] + L[i - 2]

# print('L', L)
print(L[N])
