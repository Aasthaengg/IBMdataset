S = input()
lis = [S[0]]
i = 1
while i<len(S)-1:
  if S[i]==lis[-1]:
    lis.append(S[i:i+2])
    i += 2
  else:
    lis.append(S[i])
    i += 1
ans = len(lis)
if i==len(S)-1 and S[i]!=lis[-1]:
  ans += 1
print(ans)