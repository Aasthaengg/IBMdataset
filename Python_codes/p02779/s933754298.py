import sys

N = int(sys.stdin.readline().rstrip())
A = [int(x) for x in sys.stdin.readline().rstrip().split()]

A.sort()

for i in range(N - 1):
    if A[i] == A[i + 1]:
        print("NO")
        break
else:
    print("YES")
