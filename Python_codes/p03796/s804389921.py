N=int(input())
key=1
for i in range(1,N+1):
  key=(key*i)%1000000007
print(key)