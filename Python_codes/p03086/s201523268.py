S=input()
 
acgt_list=[0]
for i in range(len(S)):
  for j in range(i+1,len(S)+1):
    slen=len(S[i:j])
    temp=0
    for s in S[i:j] :
      if s=='A' or s=='C' or s=='G' or s== 'T':
        temp+=1      
    if temp==slen:
      acgt_list.append(slen)
      
print(max(acgt_list))