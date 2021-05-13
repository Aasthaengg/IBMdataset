n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
k = sum(b)-sum(a)
if k<0:
  print("No")
  exit()
ansa=0
ansb=0
for i in range(n):
  if b[i]<a[i]:
    ansb+=a[i]-b[i]
  else:
    re = b[i]-a[i]
    if re%2==0:
      ansa+=(b[i]-a[i])//2
    else:
      ansa+=(b[i]+1-a[i])//2
      ansb+=1
if (k-ansa)*2==k-ansb and 0<=k-ansa and 0<=k-ansb:
  print("Yes")
else:
  print("No")