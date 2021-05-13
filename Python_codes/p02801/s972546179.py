C = input()
S = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(S)):
  if S[i] == C:
    break
print(S[i+1])