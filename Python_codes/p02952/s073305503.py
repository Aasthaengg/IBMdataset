a=input()
sum=0
for i in range(0,len(a)-1,2):
  sum+=9*10**i
if len(a)%2!=0:
  sum+=int(a)-10**(len(a)-1)+1
print(sum)
