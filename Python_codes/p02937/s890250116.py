import bisect
S=list(input())
T=list(input())
A=[[] for i in range(26)]
for i in range(len(S)):
  A[ord(S[i])-97].append(i+1)
a=0
b=0
for i in range(len(T)):
  k=ord(T[i])-97
  if len(A[k])==0:
    print(-1)
    exit()
  if b>=A[k][-1]:
    a=a+1
    b=A[k][0]
    continue
  else:
    b=A[k][bisect.bisect_right(A[k],b,lo=0,hi=len(A[k]))]
print(a*len(S)+b)