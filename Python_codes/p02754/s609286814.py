import os, sys
if os.environ.get("DEBUG") is not None:
    sys.stdin = open("in.txt", "r")
rl = sys.stdin.readline

n, a, b = map(int, rl().split())
print((n // (a + b)) * a + min(n % (a + b), a))