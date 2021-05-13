N,K = map(int,input().split())
num = (10**5+1)*[0]
tot = 0

for n in range(N):
  a,b=map(int,input().split())
  num[a]+=b 

for n in range(10**5+1):
  tot+=num[n]
  if K<=tot:
    print(n)
    break