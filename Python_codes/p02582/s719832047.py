S = input()
 
ans = 0
if S == 'RRR': ans = 3
else:
  if ('RR' in S): ans = 2
  else:
    if('R' in S): ans = 1
    else: ans = 0
 
print(ans)