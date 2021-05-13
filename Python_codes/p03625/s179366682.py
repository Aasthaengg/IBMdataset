N=int(input())
A=list(map(int,input().split()))
A.sort(reverse=True)
A.append(0)
i=0
ans=1
d=0
while i<N:
  b=A[i]
  c=0
  while i<N and b==A[i]:
    i+=1
    c+=1
  if 2<=c<=3:
    d+=1
    ans*=b
    if d==2:
      break
  elif 4<=c:
    if d==0:
      ans*=b*b
      d=2
      break
    else:
      ans*=b
      d+=1
      break
if d!=2:
  print(0)
else:
  print(ans)