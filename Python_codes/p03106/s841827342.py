a,b,k = map(int,input().split())
minnum = min(a,b)
maxnum = max(a,b)
lis = []
for mi in reversed(range(1,minnum+1)):
  if minnum % mi == 0 and maxnum % mi == 0:
    lis.append(mi)

print(lis[k-1])