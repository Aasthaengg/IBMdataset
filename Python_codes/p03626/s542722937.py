N=int(input())
A=input()
B=input()
C=[]
count=1
for i in range(N-1):
  if A[i]!=A[i+1]:
    C.append(count)
    count=1
  else:
    count+=1
if N==1:
  print(3)
  exit()
  
if A[-1]==A[-2]:
  C.append(2)
else:
  C.append(1)

ans=3
if C[0]==2:
  ans*=2
d=len(C)
for i in range(1,d):
  if C[i]==1 and C[i-1]==2:
    ans*=1
    ans%=10**9+7
  elif C[i]==2 and C[i-1]==2:
    ans*=3
    ans%=10**9+7
  else:
    ans*=2
    ans%=10**9+7
print(ans%(10**9+7))