n=int(input())
for i in range(5,-1,-1):
  if n//10**i: break
if i:
  s=int('90'*((i-1)//2)+'9')
else: s=0
if i%2==0:
  s+=n-10**i+1
print(s)