N = int(input())
S = 0
for i in range(1, int(N**(1/2))+1):
  if N % i == 0 and N // i > i + 1:
    S += N // i - 1
print(S)