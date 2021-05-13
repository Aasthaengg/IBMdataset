import sys

def DFS(index, tm, l, a, b):
 tm += 1
 a[index] = tm
 for i in l[index]:
  if not a[i-1]:
   tm = DFS(i-1, tm, l, a, b)
 tm += 1
 b[index] = tm
 return tm


n = input()
l=[]
for i in xrange(n):
 l.append([int(s) for s in sys.stdin.readline().split()[2:]])
a = [0] * n
b = [0] * n
tm = 0
for i in xrange(n):
 if not a[i]:
    tm = DFS(i, tm, l, a, b)

for i in xrange(n):
   print i+1, a[i], b[i]