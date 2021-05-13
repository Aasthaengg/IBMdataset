from itertools import combinations as comb
n = int(input())
l = int((2*n)**0.5)
if 2*n == l*(l+1):
  print('Yes')
  print(l+1)
  ans = [[] for i in range(l+1)]
  for i,j in zip(range(n),comb(range(l+1),2)):
    ans[j[0]].append(i+1)
    ans[j[1]].append(i+1)
  for i in ans:
    print(l,*i,sep=' ')
else:
  print('No')