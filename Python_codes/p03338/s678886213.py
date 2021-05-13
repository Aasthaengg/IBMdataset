N=int(input())
L=list(input())
maxa=-10
for i in range(N-1):
  a=set(L[:i+1])
  b=set(L[i+1:])
  maxa=max(maxa,len(a&b))
print(maxa)