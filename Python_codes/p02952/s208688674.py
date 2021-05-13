n=int(input())
res=9 if n >=9 else n
for i in range(3,len(str(n))+1):
  if i%2==0:
    continue
  res+=min(n+1,10**i)-10**(i-1)
print(res)
