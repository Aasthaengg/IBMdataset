from collections import Counter

n=int(input())
a=list(map(int,input().split()))

c=Counter(a)

def eratosthenes(lim):
  is_p=[1]*lim
  is_p[0]=1
  is_p[1]=1

  for i in set(a):
    if is_p[i]:
      for j in range(i*2,lim,i):
        is_p[j]=0

  return is_p

lim=10**6+5
is_p=eratosthenes(lim)

cnt=0
for i in a:
  if is_p[i]==1 and c[i]==1:
    cnt+=1

print(cnt)