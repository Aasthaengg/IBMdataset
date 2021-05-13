import math
n=int(input())
#generate all the primes 
def chk_prime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if n%i==0:
      return False
  return True
primes=[]
for i in range(2,n+1):
  if chk_prime(i):
    primes.append(i)
cc=[0]*len(primes)
for i in range(2,n+1):
  num=i
  for j in range(len(primes)):
    cnt=0
    while num%primes[j]==0:
      num//=primes[j]
      cnt+=1
    cc[j]+=cnt
ans=0
#count how many are of the type 75
for i in cc:
  if i>=74:
    ans+=1
#count how many are of the type 25,3
cnt_24=0
cnt_2=0
for i in cc:
  if i>=24:
    cnt_24+=1
  if i>=2:
    cnt_2+=1
ans+=cnt_24*(cnt_2-1)
#count how many are of the type 15,5
cnt_14=0
cnt_4=0
for i in cc:
  if i>=14:
    cnt_14+=1
  if i>=4:
    cnt_4+=1
ans+=cnt_14*(cnt_4-1)
#count how many are of the type 5,5,3
cnt_4=0
for i in cc:
  if i>=4:
    cnt_4+=1
ans+=((cnt_4*(cnt_4-1))//2)*(cnt_2-2)
print(ans)
