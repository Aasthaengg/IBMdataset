import sys
def Ii():return int(sys.stdin.readline())
def Mi():return map(int,sys.stdin.readline().split())
def Li():return list(map(int,sys.stdin.readline().split()))

n = Ii()
a = Li()
sa = sum(a)
af = [0]*(10**5+1)
for i in a: 
  af[i]+=1
q = Ii()
for i in range(q):
  b,c = Mi()
  sa = sa + (c-b)*af[b]
  af[c] += af[b]
  af[b] = 0;
  print(sa)