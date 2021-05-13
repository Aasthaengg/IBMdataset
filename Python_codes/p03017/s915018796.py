import sys
input = sys.stdin.readline
N, A, B, C, D = map(int, input().split())
S = list(input())[: -1]
tri = 0
for i in range(min(A, B) - 1, max(C, D) - 1):
  if S[i] == "#" and (S[i + 1] == "#"):
    print("No")
    exit(0)
for i in range(max(A, B) - 1, min(C, D)):
  if S[i] == "." and (S[i - 1] == ".") and (S[i + 1] == "."): tri = 1
if C <= D:
  print("Yes")
else:
  if tri: print("Yes")
  else: print("No")
