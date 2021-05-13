import sys
input = sys.stdin.readline
S = list(input())[: -1]
t = list("CODEFESTIVAL2016")
res = 0
for i in range(16):
  if S[i] != t[i]:
    res += 1
print(res)