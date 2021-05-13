from sys import stdin
ans=0
rans=0
c=0
check=True
S = input().rstrip()
def countans(s,rans,check):
  if (s=='A' or s=='C' ) or (s=='G'or s=='T'):
    rans+=1
  else:
    check=False
  return rans,check

for s in range(len(S)):
  rans=0
  check = True
  while True:
    if check:
      rans, check = countans(S[s],rans,check)
      if s>=len(S)-1:
        break
      s+=1
    else:
      break
  if ans<rans:
    ans =rans

print(ans)
