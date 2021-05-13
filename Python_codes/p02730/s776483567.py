S=input()
N=len(S)
l=(N-1)//2
for i in range(l):
  if S[i]!=S[N-1-i]:
    print('No')
    exit()
L=S[:l]
for i in range(l):
  if S[i]!=S[l-1-i]:
    print('No')
    exit()
print('Yes')
