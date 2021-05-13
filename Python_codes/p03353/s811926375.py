L=list()
s=input()
K=int(input())
if len(s)<10:
  for i in range(len(s)):
    for j in range(i+1,len(s)+1):
      L.append(str(s[i:j]))
  L=sorted(list(set(L)))
  print(L[K-1])
else:
  A=sorted(list(s))
  B=[A[0],A[1],A[2],A[3],A[4]]
  for i in range(len(s)):
    if s[i] in B:
      for j in range(i+1,min(i+6,len(s)+1)):
        L.append(str(s[i:j]))
      L=sorted(list(set(L)))
      if len(L)>K:
        L=list(L[:K])
  print(L[K-1])