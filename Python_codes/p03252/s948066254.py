from collections import Counter

S=list(input())
T=list(input())
a=Counter(S).most_common()
b=Counter(T).most_common()
for i in range(len(a)):
  if a[i][1]!=b[i][1]:
    print('No')
    exit()
else:
  print('Yes')