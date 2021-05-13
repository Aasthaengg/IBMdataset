x,y,a,b,c,=map(int,input().split())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
r=list(map(int,input().split()))
p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)
p=p[:x]
q=q[:y]
ans=p+q
ans.sort(reverse=True)
ans=[0]+ans
nowi=x+y
r=[0]+r
nowr=0
while nowr<=c-1 and nowi>0 and r[nowr+1]>ans[nowi]:
  nowi+=-1
  nowr+=1
ans_=0
for i in range(nowi+1):
  ans_+=ans[i]
for j in range(nowr+1):
  ans_+=r[j]
print(ans_)
