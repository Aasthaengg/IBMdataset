#import numpy

#for loop
#a = [1,2,3,4,5,6,7,8,9,10]
#s = [0]*len(a)
#s[0] = a[0]
#for i in range(len(a)-1):
#  s[i+1] = s[i] + a[i+1]
#print(s)

#numpy.cumsum()
#print(numpy.cumsum(a))

q = int(input())
n = 10**5+1
limit = int(n**0.5)
a = [i for i in range(3, n, 2)]
prime = [2]
while True:
  p = a[0]
  if limit <= p:
    prime += a
    break
  prime.append(p)
  a = [j for j in a if j%p!=0]
  
pi = [0]*n
for i in range(len(prime)):
  ai = (prime[i]+1)//2
  if ai in prime:
    pi[prime[i]-1] = 1
    
s = [0]*n
s[0] = pi[0]
for i in range(len(pi)-1):
  s[i+1] = s[i] + pi[i+1]
s = [0,0] + s
for i in range(q):
  l, r = map(int, input().split())
  print(s[r+1]-s[l])
