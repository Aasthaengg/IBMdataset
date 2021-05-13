import sys

N=int(input())
A=list(map(int,input().split()))
div_flg=False
inc_flg=False
dec_flg=False
ans=0

if N==1:
  print(1)
  sys.exit()
  
for i in range(N):
  if inc_flg:
    if i==N-1:
      break
    if A[i]<=A[i+1]:
      continue
    else:
      inc_flg=False
      div_flg=False
  elif dec_flg:
    if i==N-1:
      break
    if A[i]>=A[i+1]:
      continue
    else:
      dec_flg=False
      div_flg=False
  else:
    if i==0:
      ans+=1
      div_flg=True
    elif i==N-1:
      if not div_flg:
        ans+=1
      break
    if A[i]==A[i+1]:
      if not div_flg:
        ans+=1
      div_flg=True
      continue
    elif A[i]<A[i+1]:
      if not div_flg:
        ans+=1
      inc_flg=True
      continue
    elif A[i]>A[i+1]:
      if not div_flg:
        ans+=1
      dec_flg=True
      continue
print(ans)