from collections import defaultdict
N=int(input())

### 関数＆defaultdict版
def factorize(M):
  res=defaultdict(int)
  #for i in range(2,int(M**0.5)+1):
  for i in prime_list:  
    if M==1:
      break
    while M%i==0:
      M//=i
      res[i]+=1  
  if M!=1:
    res[M]=1
  return res

# n"未満"の素数のリストを得る
def prime_sieve(n):
  prime_list=[True]*n
  prime_list[0]=False
  prime_list[1]=False
  for i in range(2,int(n**0.5)+1):
    if not prime_list[i]:
      continue
    else:
      for j in range(i**2,n,i):
        prime_list[j]=False
  return [i for i in range(n) if prime_list[i]]

prime_list=prime_sieve(int(N**0.5)+1)
answer=0
for i in range(1,N):
  facts=factorize(i)
  
  num_div=1
  for k,v in facts.items():
    num_div*=v+1
  answer+=num_div
  
print(answer)