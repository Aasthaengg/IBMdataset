S = input()
rt = 0
for l in range(1,len(S)+1):
  for i in range(len(S)-l+1):
    tmp = 1 if i == 0 or i+l==len(S) else 2
    tw = 2**(0 if len(S)-l-tmp<0 else len(S)-l-tmp)
    rt+=tw*int(S[i:i+l])

print(rt)