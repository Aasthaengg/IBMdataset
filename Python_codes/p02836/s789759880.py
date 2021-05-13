S = input()
k = len(S)//2
res = 0
for i in range(k):
  if S[i]!=S[len(S)-1-i]:
    res += 1
print(res)