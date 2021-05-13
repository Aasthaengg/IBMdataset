S=list(input())
k=int(input())
Ans=[0]*len(S)
c=0
for i in range(len(S)):
  if (26-(ord(S[i])-97))%26<=k:
    Ans[i]="a"
    k=k-(26-(ord(S[i])-97))%26
    c=c+(26-(ord(S[i])-97))%26
  else:
    Ans[i]=S[i]
  if i==len(S)-1:
    c=ord(Ans[i])+k%26
    if ord(Ans[i])+k%26>=123:
      c=c-26
    Ans[i]=chr(c)
print("".join(Ans))