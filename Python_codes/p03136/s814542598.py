import sys

input = sys.stdin.readline
N = int(input())
L = list(map(int, input().split()))

L.sort()
if sum(L[:N-1]) > L[N-1]:
    print("Yes")
else:
    print("No")