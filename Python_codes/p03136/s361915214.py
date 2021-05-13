n = int(input())
L = list(map(int,input().split()))
L2 = sorted(L)
L3 = sum(L) - L2[n-1]
if(L3 > L2[n-1]):
  print('Yes')
else:
  print('No')