N=input()
p=N if N%2 else N+1
ls = []
for i in range(N):
 for j in range(i + 1, N):
  if i+j +2 != p:
   ls += [(i+1, j+1)]

print len(ls)
for a,b in ls:
 print a, b