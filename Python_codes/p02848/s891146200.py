N=int(input())
S=input()
L=list(S)
A=len(L)
S=[]
for i in range(A):
  if (ord(L[i])+N)>90:
    S.append(chr(ord(L[i])+N-26))
  else:
    S.append(chr(ord(L[i])+N))
    
print(''.join(S))