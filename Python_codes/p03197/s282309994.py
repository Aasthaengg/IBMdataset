import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
  if int(input()) % 2:
    print("first")
    exit(0)
print("second")