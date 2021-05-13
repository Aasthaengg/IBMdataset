q=int(input())

#prime table
prime=[0 for i in range(10**5+5)]
for i in range(2,10**5+5):
  j=1
  if not prime[i]:
    while j*i<=10**5+4:
      prime[j*i]=i
      j+=1

like2017=[0 for i in range(10**5+5)]
for i in range(3,10**5+5,2):
  j=(i+1)//2
  if i==prime[i] and j==prime[j]:
    like2017[i]=1

like2017sum=[0 for i in range(10**5+5)]
for i in range(10**5+4):
  like2017sum[i+1]=like2017sum[i]+like2017[i+1]
#print(like2017[0:54])
#print(like2017sum[0:80])
for i in range(q):
  l,r=map(int,input().split())
  if like2017[l]==1:
    alpha=1
  else:
    alpha=0
  print(like2017sum[r]-like2017sum[l]+alpha)
