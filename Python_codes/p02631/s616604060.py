import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
X = 0

for ai in a:
    X ^= ai

ans = [X^ai for ai in a]
print(*ans)