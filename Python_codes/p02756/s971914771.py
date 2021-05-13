S=input()
p=1
head=""
tail=""
Q=int(input())
for _ in range(Q):
  q=input()
  if q=='1':
    p^=1
  else:
    a,f,c=q.split()
    f=int(f)%2
    if p==0:
      f=(f+1)%2
    if f:
      head+=c
    else:
      tail+=c
if p:
  S=head[::-1]+S+tail
else:
  S=tail[::-1]+S[::-1]+head
print(S)