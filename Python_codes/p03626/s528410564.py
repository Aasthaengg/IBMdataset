n=int(input())
A=input()
B=input()
ans=1
i=0
while i<n:
  if A[i]==B[i]:
    if i==0:
      ans=ans*3
    elif a==1:
      ans=ans*2
    else:
      ans=ans
    i=i+1
    a=1
  else:
    if i==0:
      ans=ans*6
    elif a==1:
      ans=ans*2
    else:
      ans=ans*3
    i=i+2
    a=2
print(ans%(10**9+7))