n,t=map(int,input().split())
a=list(map(int,input().split()))
b=[]
min_a=a[0]
cnt_min=1
for ai in a[1:]:
  if min_a<ai:
    b.append([ai,ai-min_a,cnt_min])
  elif min_a==ai:
    cnt_min+=1
  elif min_a>ai:
    cnt_min=1
    min_a=ai

b.sort(key=lambda x:x[1])
max_v=b[-1][1]
ans={}
while b and max_v==b[-1][1]:
  d,v,e=b.pop()
  if d in ans:
    if e==ans[d][0]:
      ans[d]=[e,ans[d][1]+1]
    elif e>ans[d][0]:
      ans[d]=[e,1]
    else:
      pass
  else:
    ans[d]=[e,1]
tmp=0
for v in ans.values():
  tmp+=min(v)
print(tmp)
