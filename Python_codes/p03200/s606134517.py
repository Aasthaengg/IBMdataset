S=[x for x in input()]
ans=0
W_cnt=S.count('W')

for s in S:
  if s=='W':
    W_cnt-=1
  elif s=='B':
    ans+=W_cnt
print(ans)