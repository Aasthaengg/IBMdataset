import numpy as np
def seachPrimeNum(N):
  max = int(np.sqrt(N))
  seachList = [i for i in range(2,N+1)]
  primeNum = []
  while seachList[0] <= max:
    primeNum.append(seachList[0])
    tmp = seachList[0]
    seachList = [i for i in seachList if i % tmp != 0]
  primeNum.extend(seachList)
  return primeNum

n=10**5
a=seachPrimeNum(n)
b=[]
y=0
x=0
while x<=100000:
  t=a[y]
  x=t*2-1
  b.append(x)
  y+=1
  
c=set(a)&set(b)

q=int(input())
r=[0 for _ in range(100000)]
for f in c:
  r[f]=1
for g in range(len(r)-1):
  r[g+1]=r[g]+r[g+1]

for p in range(q):
  w,z=map(int,input().split())
  print(r[z]-r[w-1])

