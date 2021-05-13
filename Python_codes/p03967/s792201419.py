s=input().rstrip()
win,lose=0,0
if s[0] == 'p':
  lose += 1
countg,countp=1,0
for i in range(1,len(s)):
  if s[i] =='g' and (countp +1 <= countg):
    win += 1
    countp += 1
  elif s[i] =='g':
    countg += 1
  elif s[i] =='p' and (countp +1 <= countg):
    countp += 1
  else:
    countg += 1
    lose += 1
print(win-lose)