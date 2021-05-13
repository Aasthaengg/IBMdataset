n=[]
r,d,x=map(int,input().split())
n.append(x)
def m(i):
  return r*i-d
for i in range(10):
  n.append(m(n[i]))
  print(n[-1])