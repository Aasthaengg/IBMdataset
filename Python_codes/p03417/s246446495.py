N,M=map(int,input().split())

ANS = 0
if N != 1 and M != 1:
  ANS = N * M - (2 * N + 2 * M -4)
elif N == 1 and M == 1:
  ANS = 1
else:
  ANS = N * M - 2
print(ANS)