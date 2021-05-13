from itertools import groupby

s = list(input())
ans = [0]*len(s)
ind = 0

for k,v in groupby(s):
  key,value = k,len(list(v))
  ind += value
  
  if k == 'R':
    if value%2 != 0:
      ans[ind-1] += (value//2)+1
      ans[ind] += value//2
    else:
      ans[ind-1] += value//2
      ans[ind] += value//2
  else:
    if value%2 != 0:
      ans[ind -value] += (value//2) + 1
      ans[ind-1- value] += (value//2) 
    else:
      ans[ind -value] += value//2
      ans[ind -1- value] += value//2
      
print(*ans)