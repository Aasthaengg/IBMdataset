import sys
readline = sys.stdin.readline

N = int(readline())
S = readline().rstrip()
T = readline().rstrip()

for i in range(N, -1, -1):
#  print("i",i)
#  print(S[-i:],T[:i])
  if S[-i:] == T[:i]:
    print(N * 2 - i)
    break
else:
  print(N * 2)