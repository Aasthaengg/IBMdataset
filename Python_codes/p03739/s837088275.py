n=int(input())
a=list(map(int,input().split()))
ans_o=0
cnt_o=0
ans_e=0
cnt_e=0
for i in range(n):
  cnt_o+=a[i]
  if i%2==0:
    if cnt_o>0:
      continue
    else:
      ans_o+=abs(cnt_o)+1
      cnt_o=1
  else:
    if cnt_o<0:
      continue
    else:
      ans_o+=cnt_o+1
      cnt_o=-1
for i in range(n):
  cnt_e+=a[i]
  if i%2==0:
    if cnt_e<0:
      continue
    else:
      ans_e+=cnt_e+1
      cnt_e=-1
  else:
    if cnt_e>0:
      continue
    else:
      ans_e+=abs(cnt_e)+1
      cnt_e=1
print(min(ans_o,ans_e))