s=int(input())
a=[0]*1000000
a[s-1]+=1
i=1
while True:
  i+=1
  if s%2==0:
    s=s//2
  else:
    s=3*s+1
  a[s-1]+=1
  if a[s-1]==2:
    print(i)
    break
