s=list(input())[::-1]

s_cnt=0
t_cnt=0


for ss in s:
  if ss=="S":
    if t_cnt>0:
      t_cnt-=1
    else:
      s_cnt+=1
  else:
    t_cnt+=1
print(t_cnt+s_cnt)

