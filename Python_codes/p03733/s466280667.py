n,t=map(int,input().split())
tl=list(map(int,input().split()))+[10**10]

ans=0
bef=0
for i in range(1,n+1):
  t_ans=t
  e_time=tl[i-1]+t
  if e_time>tl[i]:
    t_ans-=e_time-tl[i]
  ans+=t_ans
print(ans)