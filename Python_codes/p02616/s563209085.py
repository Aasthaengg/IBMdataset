MOD=10**9+7
N,K=[int(s) for s in input().split()]
ls=[int(s) for s in input().split()]
ls=sorted(ls, key=lambda x: -abs(x))

#かける数をフラグで管理
flag=[0 for _ in range(N)]

sign=0
for i in range(K):
  flag[i]=1
  if ls[i]<0:
    sign=(sign+1)%2

if sign==1: #絶対値が大きい順にかけた数は負か？
  #フラグのない負の数を、フラグのある正の数と取り換え可能か？
  swap_neg_to_pos=[]
  for i in range(K,N):
    if ls[i]<0:
      for j in range(K):
        if ls[K-1-j]>0:
          swap_neg_to_pos=[i,K-1-j,ls[K-1-j],-ls[i]]
          break
      break
  #フラグのない正の数を、フラグのある負の数と取り換え可能か？
  swap_pos_to_neg=[]
  for i in range(K,N):
    if ls[i]>0:
      for j in range(K):
        if ls[K-1-j]<0:
          swap_pos_to_neg=[i,K-1-j,-ls[K-1-j],ls[i]]
          break
      break

  #フラグを修正        
  if swap_neg_to_pos!=[] and swap_pos_to_neg!=[]: #どちらも取り換え可能なとき
    #負の数にフラグを与えたほうがロスが少ないとき
    if swap_neg_to_pos[2]*swap_pos_to_neg[3]<swap_pos_to_neg[2]*swap_neg_to_pos[3]: 
      flag[swap_neg_to_pos[0]]=1
      flag[swap_neg_to_pos[1]]=0
    else: #正の数にフラグを与えたほうがロスが少ないとき
      flag[swap_pos_to_neg[0]]=1
      flag[swap_pos_to_neg[1]]=0
  elif swap_neg_to_pos==[] and swap_pos_to_neg==[]: #どちらも取り換え不可能なとき 
    flag.reverse()
  elif swap_pos_to_neg!=[]: #正の数にフラグを与えることのみ可能なとき
    flag[swap_pos_to_neg[0]]=1
    flag[swap_pos_to_neg[1]]=0
  else:                     #負の数にフラグを与えることのみ可能なとき
    flag[swap_neg_to_pos[0]]=1
    flag[swap_neg_to_pos[1]]=0

ans=1
for i in range(N):
  if flag[i]==1:
    ans=(ans*ls[i])%MOD
print(ans)
