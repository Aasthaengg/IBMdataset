n = str(input())
ans = []
for i in n : 
  ans.append(int(i))
if sum(ans) % 9 == 0 : 
  print('Yes')
else : 
  print('No')