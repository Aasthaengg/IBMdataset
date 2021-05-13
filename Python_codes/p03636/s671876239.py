import sys
stdin = sys.stdin
sys.setrecursionlimit(10 ** 7)

i_i = lambda: int(i_s())
i_l = lambda: list(map(int, stdin.readline().split()))
i_s = lambda: stdin.readline().rstrip()

s = i_s()
print(s[0] + str(len(s)-2) + s[-1])