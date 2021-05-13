s=list(input())
n=len(s)
for i in range(n):
  s[i]=int(s[i])
dec_flg=0
for i in range(n):
  if i==0:continue
  if dec_flg==0:
    if 0<=s[i]<=8 and s[i-1]>0:
      s[i-1]-=1
      s[i]=9
      dec_flg=1
  else:
    if 0<=s[i]<=8:
      s[i]=9
ans=0
for ss in s:
  ans+=ss
print(ans)