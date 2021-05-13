S=[]
while True:
  m,f,r=map(int,input().split())
  if m==-1 and f==-1 and r==-1:
    break
  if m==-1 or f==-1 or m+f<30:
    S.append('F')
  elif m+f>=80:
    S.append('A')
  elif 65<=m+f<80:
    S.append("B")
  elif 50<=m+f<65:
    S.append("C")
  else:
    if r>=50:
      S.append("C")
    else:
      S.append("D")
    
  k=int(0)  
for i in S:
  print(S[k])
  k=k+1  
