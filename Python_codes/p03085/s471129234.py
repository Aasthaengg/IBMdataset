import sys
input = sys.stdin.readline
S = input()[: -1]
t = ["A", "C", "G", "T"]
for i in range(4):
  if S == t[i]:
    print(t[-1 - i])
    exit(0)