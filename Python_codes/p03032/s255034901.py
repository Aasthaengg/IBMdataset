from collections import deque
n,k=map(int,input().split())
v=list(map(int,input().split()))
cs_l=[0]
cs_r=[0]
cs1,cs2=0,0
for i in range(n):
  cs1+=v[i]
  cs2+=v[-i-1]
  cs_l.append(cs1)
  cs_r.append(cs2)

ans=0
for i in range(1,k+1):# 取得する操作をi回行う
  for l in range(i+1): # 左からl個取る
    r=i-l
    if r+l>=n:
      point=cs_r[-1]
      minus=[vi for vi in v if vi<0]
      n_minus=min(n-k,len(minus))
    else:
      point=cs_l[l]+cs_r[r]
      minus=[vi for vi in v[:l] if vi<0]
      if r>0:
        minus+=[vi for vi in v[-r:] if vi<0]
      n_minus=min(k-r-l,len(minus))
    if n_minus>0:
      minus.sort()
      point-=sum(minus[:n_minus])
    ans=max(ans,point)

print(ans)

