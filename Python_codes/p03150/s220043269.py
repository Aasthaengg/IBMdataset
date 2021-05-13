A=["k","e","y","e","n","c","e"]
f=-1;p=0
S=list(map(str,input()))
if S[0:7]==A or S[len(S)-7:len(S)]==A:
  f=1
else:
  if S[0]!=A[0]:
    f=0
  else:    
    for i in range(len(S)):
      if S[i]==A[i]:
        p=p+1
      else:
        if A[0:p]+S[len(S)-(len(A)-p):len(S)]==A:
          f=1
          break
        else:
          f=0
          break
print("YES" if f==1 else "NO")