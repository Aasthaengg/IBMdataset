S=str(input())
S=list(map(str,S))
count=0
real_count=0
for i in range(len(S)):
  if S[i]=='A' or S[i]=='C' or S[i]=='G' or S[i]=='T':
    for j in range(i,len(S)):
      if S[j]=='A' or S[j]=='C' or S[j]=='G' or S[j]=='T':
        count+=1
      else:
        break
    if count>real_count:
      real_count=count
    count=0
print(real_count)