from collections import Counter
n = int(input())
v = list(map(int,input().split()))
v1 = v[::2]
v2 = v[1::2]
C1 = Counter(v1)
C2 = Counter(v2)
if C1.most_common(1)[0][0]!=C2.most_common(1)[0][0]: 
  print((n//2-C1.most_common(1)[0][1])+(n//2-C2.most_common(1)[0][1]))
elif C1.most_common(1)[0][1]==C2.most_common(1)[0][1]==n//2:
  print(n//2)
elif C1.most_common(1)==C2.most_common(1) and C1.most_common(2)[1][1] >= C2.most_common(2)[1][1]:
  print((n//2-C1.most_common(2)[1][1])+(n//2-C2.most_common(1)[0][1]))
else:
  print((n//2-C1.most_common(1)[0][1])+(n//2-C2.most_common(2)[1][1]))
 