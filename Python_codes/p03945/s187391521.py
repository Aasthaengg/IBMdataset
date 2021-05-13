ans = []
S=list(input())
for i in range(len(S)-1):
  if S[i] != S[i+1]:
    ans.append(S[i])
print(ans.count("W")+ans.count("B"))