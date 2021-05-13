H,W=map(int,input().split())
flg=0
flg2=0
bef=[];aft=[]
ans=[]
N=0
for i in range(H):
  flg+=1;flg%=2
  A=list(map(int,input().split()))
  if flg==1:
    for j in range(W):
      a=A[j]
      aft=[i+1,j+1]
      if a%2==0:
        if flg2==0:
          pass
        else:
          ans.append(bef+aft)
          N+=1
      else:
        if flg2==0:
          flg2=1
        else:
          ans.append(bef+aft)
          N+=1
          flg2=0
      bef=[i+1,j+1]
          
  else:
    for j in range(W-1,-1,-1):
      a=A[j]
      aft=[i+1,j+1]
      if a%2==0:
        if flg2==0:
          pass
        else:
          ans.append(bef+aft)
          N+=1
      else:
        if flg2==0:
          flg2=1
        else:
          ans.append(bef+aft)
          N+=1
          flg2=0
      bef=[i+1,j+1]
print(N)
for i in ans:
  print(*i)