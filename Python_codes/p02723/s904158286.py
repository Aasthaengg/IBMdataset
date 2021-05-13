import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))

s = ins()
print("Yes" if s[2] == s[3] and s[4] == s[5] else "No")