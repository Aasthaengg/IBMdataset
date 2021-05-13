from collections import defaultdict
N=int(input())
h=[]
a=list(map(int,input().split()))
cnt_dic=defaultdict(int)
for i in range(N):
  cnt_dic[a[i]]+=1
cnt_l=sorted(cnt_dic.values(),reverse=True)
ans=len(cnt_l)
tmp=0
for i in range(ans):
  if cnt_l[i]%2==0:
    tmp+=1
if tmp%2==0:
  pass
else:
  ans-=1
print(ans)