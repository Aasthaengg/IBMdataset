S=input()
K=int(input())
N=len(S)

if S.count(S[0])==N:
  ans= K*N//2
else:
  h=0
  for i in range(N):
    if S[i]==S[0]:
      h +=1
    else:
      break
  t=0
  for i in range(N-1,-1,-1):
    if S[i]==S[-1]:
      t +=1
    else:
      break
  ren=1
  cnt=0
  for i in range(h,N-t):
    if S[i]==S[i-1]:
      ren +=1
      if i==N-t-1:
        cnt += ren//2
    else:
      cnt += ren//2
      ren=1    
      
  if S[0]==S[-1]:
    #print(h//2, (K-1)*((h+t)//2), t//2 ,K*cnt)
    ans= h//2 + (K-1)*((h+t)//2) + t//2 + K*cnt
  else:
    #print(h//2,cnt,t//2)
    ans= (h//2 + cnt + t//2)*K
print(ans)