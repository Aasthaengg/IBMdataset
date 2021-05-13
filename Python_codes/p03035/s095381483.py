import sys
input = lambda : sys.stdin.readline().rstrip()

a, b = map(int, input().split())

ans = 0 if a <= 5 else b//2 if a <= 12 else b

print(ans)