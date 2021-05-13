MM = input()
listM = list(MM)
xx = len(listM)
saisyo =0
saigo  =xx
xx = len(listM)
for i in range(0,xx-1,1):
  
  if listM[i]=='A':
    saisyo = i
    
    break
for i in range(xx-1,0,-1):
  
  if listM[i]=='Z':
    saigo = i
    
    break
ans = saigo -saisyo
print(ans+1)