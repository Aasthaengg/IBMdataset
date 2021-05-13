import sys
input = sys.stdin.readline
S = list(input())[: -1]
print(S[0] + str(len(S) - 2) + S[-1])