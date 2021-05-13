import sys
int1 = lambda x: int(x) - 1
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)


def dfs(s, c):
    if len(s) == N:
        print(s)
    else:
        for ch in range(97, ord(c) + 1):
            dfs(s + chr(ch), chr(ord(c) + 1) if chr(ch) == c else c)


N = int(read())
dfs("", "a")
