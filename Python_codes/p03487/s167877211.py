from collections import Counter
n=int(input())
a=Counter(list(map(int,input().split())))
cnt=0
for i,j in a.most_common():
  if i<=j:cnt+=j-i
  else:cnt+=j
print(cnt)