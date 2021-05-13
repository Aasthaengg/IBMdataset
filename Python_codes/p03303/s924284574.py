import sys
input = sys.stdin.readline
S = list(input())[: -1]
w = int(input())
print("".join(S[: : w]))