import re
s=input()
n=len(s)
ans=0
for i in range(n):
  for j in range(n):
    S=s[i:j+1]
    #print(S)
    m=re.fullmatch(r'[ATCG]+',S)
    #print(m)
    if m!=None:
      ans=max(ans,len(S))
print(ans)