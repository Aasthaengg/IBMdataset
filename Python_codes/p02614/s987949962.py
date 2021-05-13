import copy
H,W,K=map(int,input().split())
L=[]
for i in range(H):
  L_=list(input())
  L.append(L_)

cnt=0
for i in  range(2**H):
  l=copy.deepcopy(L)
  
  for k in range(H):
    if (i>>k)&1:
      l[k]=['.']*W
    
  for j in range(2**W):
    ll=copy.deepcopy(l)
   
    for m in range(W):
      if (j>>m)&1:
        for n in range(H):
          if ll[n][m]=='#':
            ll[n][m]='.'
            
    counted=0
    for o in range(H):
      counted+=ll[o].count('#')
    #print(ll)
    if counted==K:
      cnt+=1    

print(cnt)