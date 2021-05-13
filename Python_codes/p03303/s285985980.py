S = input()
w = int(input())
N = len(S)
for i in range(0, N, w):
  print(S[i], end = '')
print()