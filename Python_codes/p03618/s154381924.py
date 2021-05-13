S = input()
alp = [chr(ord('a') + i) for i in range(26)]
L = [0]*26
def alp(n):
  return(ord(n)-97)
for i in range(len(S)):
  k = alp(S[i])
  L[k] += 1
ans = len(S)*(len(S)-1)//2+1
for i in range(26):
  ans -= L[i]*(L[i]-1)//2
print(ans)