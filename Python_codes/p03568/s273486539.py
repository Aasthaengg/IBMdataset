import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

T = 1
for i in range(N):
    if A[i] % 2 == 0:
        T = T * 2
print(3**N - T)
