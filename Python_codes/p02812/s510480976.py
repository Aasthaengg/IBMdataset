N=int(input())
S=str(input())
S=S.replace('ABC','')
if N==len(S):
  print(0)
else:
  print((N-len(S))//3)