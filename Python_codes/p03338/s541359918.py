N = int(input())
S = input()

mmax = 0
for i in range(2, N-1):
  a = set(S[:i])
  b = set(S[i:])
  mmax = max(len(a&b), mmax)
print(mmax)