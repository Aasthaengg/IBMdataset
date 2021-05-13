from collections import Counter
N=int(input())
C=Counter(list(map(int, input().split())))
# print(C)
ans=0
for i in C:
  j=C[i]
  if j>=i:
    ans+=j-i
  else:
    ans+=j
print(ans)