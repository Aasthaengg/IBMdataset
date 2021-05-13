import sys
input = lambda: sys.stdin.readline().rstrip()

A,B,T = map(int, input().split())

T = T + 0.5

times = T // A

print(int(B*times))