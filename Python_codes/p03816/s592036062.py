N=int(input())
A=list(map(int, input().split()))
from collections import Counter
A=Counter(A)
tot = len(A)
cnt=0
for i in A.most_common():
  if i[1]%2==0:
    cnt+=1
print(tot-cnt%2)