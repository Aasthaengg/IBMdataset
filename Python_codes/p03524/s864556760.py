from math import ceil

S=input()
N=len(S)
a=S.count("a")
b=S.count("b")
c=S.count("c")

maxi=max(a,b,c)
mini=min(a,b,c)
midi=a+b+c-maxi-mini

ans="NO"
if maxi<=ceil(N/3):
  if midi<=ceil(N/3):
    if mini<=ceil(N/3):
      ans="YES"
      
print(ans)