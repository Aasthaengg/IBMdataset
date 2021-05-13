n,q = map(int,input().split())
s = input()
table = [0]*n
temp = s[0]
for i in range(1,n):
  table[i] = table[i-1]
  if temp=='A' and s[i]=='C':
    table[i]+=1
  temp = s[i]
for _ in range(q):
  l,r = map(int,input().split())
  print(table[r-1]-table[l-1])