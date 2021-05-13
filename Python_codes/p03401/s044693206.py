N=int(input())
A=[0]+list(map(int, input().split()))+[0]
s=sum(abs(A[i+1]-A[i]) for i in range(N+1))
for i in range(1,N+1):
  a=A[i-1]
  b=A[i]
  c=A[i+1]
  if b<a and b<c:
    ans=s-abs(b-min(a,c))*2
  elif b>a and b>c:
    ans=s-abs(b-max(a,c))*2
  else:
    ans=s
  print(ans)