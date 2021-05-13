N=input()
NL=len(N)
if N[1:]=='9'*(NL-1):
  ans=int(N[0])+9*(NL-1)
else:
  ans=int(N[0])+9*(NL-1)-1
print(ans)