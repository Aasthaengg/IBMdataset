import sys
N = int(input())
A = [int(sys.stdin.readline()) for _ in range(N)]

for a in A:
    if a % 2:
        print("first")
        break
else:
    print("second")
