import bisect
def seive():
  l[0]=0
  l[1]=0
  for i in range(2,10**6+1):
    if l[i]==1:
      k.append(i)
      for j in range(i*i,10**6+1,i):
        l[j]=0
l=[1]*(10**6+1)
k=[]
seive()
#print(len(k))
n=int(input())
d=bisect.bisect_left(k,n)
print(k[d])

