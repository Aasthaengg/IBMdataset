s=int(input())
cnt=1
x=[s]
while True:
  cnt+=1
  if s%2==0:
    s//=2
  else:
    s=3*s+1
  if s not in x:
    x.append(s)
  else:
    print(cnt)
    break