import sys
input = sys.stdin.readline

a, b, c = [int(x) for x in input().split()]

ans = "Yes" if a <= c <= b else "No"

print(ans)