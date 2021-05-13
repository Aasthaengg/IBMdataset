S=list(input())
T=list(input())
S=sorted(S)
s="".join(S)
T=sorted(T,reverse=True)
t="".join(T)
if s<t:
  print("Yes")
else:
  print("No")