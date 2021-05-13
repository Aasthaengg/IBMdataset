S = input()
N = len(S) // 2
for i in reversed(range(N)):
  if S[0:i] == S[i:2*i]:
    print(2*i)
    break