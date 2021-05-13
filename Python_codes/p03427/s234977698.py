S = input()
N = int(S)
K = len(S)
c = int(S[0])

if len(S) == 1:
  ans = c
elif (N+1)/(10**(K-1))-1 == c:
  ans = c + 9*(K-1)
else:
  ans = (c-1) + 9*(K-1)

print(ans)