S=list(input())
K=int(input())
N=len(S)
for i in range(N):
  k=(ord('z')-ord(S[i])+1)%26
  if K>=k:
    S[i]='a'
    K-=k
S[-1]=chr(ord(S[-1])+K%26)
print(''.join(S))