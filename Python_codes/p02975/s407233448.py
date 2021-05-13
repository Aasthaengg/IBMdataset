from collections import Counter
N = int(input())
a = list(map(int, input().split()))
c = Counter(a)
m = c.most_common()

if (len(m)==1) and (m[0][0]==0):
  print('Yes')
elif (m[0][1]==2*N//3) and (m[1][0]==0) and (len(m)==2):
  print('Yes')
elif (m[0][1]==N//3) and (m[1][1]==N//3) and (m[2][1]==N//3) and (m[0][0]^m[1][0]^m[2][0]==0):
  print('Yes')
else:
  print('No')