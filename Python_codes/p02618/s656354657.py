D=int(input())
c=list(map(int,input().split()))
last = [0] * 26
S=0
for d in range(1,D+1):
  s=list(map(int,input().split()))
  decline=0
  for j in range(26):
    decline += c[j]*(d-last[j])
  exp=S - decline + c[0]*(d-last[0]) + s[0]
  t=0
  for j in range(1,26):
    tmp = S - decline + c[j]*(d-last[j])+s[j]
    if tmp > exp:
      t=j
      exp=tmp
  S = exp
  last[t]=d
  print(t+1)