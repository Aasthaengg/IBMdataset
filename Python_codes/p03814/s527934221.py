S=list(input())
a=S.index("A")
n=len(S)
for i in range(n):
  if S[n-1-i]=="Z":
    k=n-1-i
    break
print(k-a+1)