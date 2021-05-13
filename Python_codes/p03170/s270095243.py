import sys
input = sys.stdin.readline
n, k = map(int,input().split())
A = list(map(int,input().split()))

D = [0] * (k+1)
for i in range(k+1):
    safe = 0
    for j in range(n):
        if i-A[j] >= 0 and D[i-A[j]] == 0:
            safe = 1
    D[i] = safe

print("First" if D[-1]==1 else "Second")