import sys

n = int(input())
A = list(map(int, sys.stdin.readline().split()))

ans = [0] * n

for i in A:
    ans[i-1] += 1

for j in ans:
    print(j)