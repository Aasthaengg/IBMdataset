s=int(input())
l=[0,0,1]
for i in range(3,s):
  l.append((l[i-1]+l[i-3])%(10**9+7))
print(l[s-1]%(10**9+7))