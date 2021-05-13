
N,M=[int(x) for x in str(input()).split()]
lim=int(M**0.5)+100005




num=10**9+7
x=1
factorial=[1]
for i in range(1,2*10**5+1):
  x=(i*x)%num
  factorial.append(x)
 
rfactorial=[]
for i in factorial:
  rfactorial.append(pow(i,num-2,num))
 

def c(n,k):
  return (((factorial[n]*rfactorial[k])%num)*rfactorial[n-k])%num


ans=1
for i in range(2,int(M**0.5)+2):
  count=0
  while M%i==0:
    count+=1
    M=M//i
  ans=(ans*c(N+count-1,count))%num
if M>1:
  ans=(ans*c(N,1))%num

print(ans)