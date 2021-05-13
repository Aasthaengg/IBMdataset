S=input()
l=len(S)
ans=0
for bit in range(2**(l-1)):
  temp=S[0]
  for i in range(l-1):
    if bit>>i&1:
      temp+="+"+S[i+1]
    else:
      temp+=S[i+1]
  ans+=eval(temp)
print(ans)
