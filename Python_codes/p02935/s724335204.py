import sys
n = int(input())
v = list(map(int,input().split()))
v.sort()
ans,tmp = [],[]
gab = (v[0]+v[1])/2
tmp.append(gab)
j = 0
if n == 2:
  print(tmp[0])
  sys.exit()
for i in range(2,n):
  tmp.append((v[i] +tmp[j])/2)
  j += 1
print(tmp[-1])