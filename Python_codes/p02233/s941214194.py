import sys
input = sys.stdin.readline

n = int(input())
F = [1]*50
for i in range(2, n+1):
    F[i] = F[i-1] + F[i-2]

print(F[n])
