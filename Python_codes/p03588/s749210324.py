import sys
input = sys.stdin.readline

N = int(input())

max_a = 0
res = 0

for _ in range(N):
    a, b = map(int, input().split())
    if max_a < a:
        max_a = a
        res = a + b

print(res)