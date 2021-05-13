import sys
  
def dfs(i, t, l, a, b):
   t += 1
   a[i] = t
   for j in l[i]:
      if not a[j-1]:
         t = dfs(j-1, t, l, a, b)
   t += 1
   b[i] = t
   return t
  
  
n = input()
l=[]
for i in range(n):
   l.append([int(s) for s in sys.stdin.readline().split()[2:]])
a = [0] * n
b = [0] * n
t = 0
for i in xrange(n):
   if not a[i]:
      t = dfs(i, t, l, a, b)
  
for i in xrange(n):
   print i+1, a[i], b[i] 