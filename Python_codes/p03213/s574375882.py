n=int(input())
m=[0]*101
for i in range(1,n+1):
  for j in range(2,n+1):
    while i%j==0:
      a=i//j
      while (a+1)*j<=i:
        a+=1
      i=a
      m[j]+=1
counter75=0
counter25=0
counter15=0
counter5=0
counter3=0
for i in range(101):
  if m[i]>=74:
    counter75+=1
  if m[i]>=24:
    counter25+=1
  if m[i]>=14:
    counter15+=1
  if m[i]>=4:
    counter5+=1
  if m[i]>=2:
    counter3+=1
a=(counter5*(counter5-1)*(counter3-2))//2
while (a+1)*2<=(counter5*(counter5-1)*(counter3-2)):
  a+=1
print(counter75+counter25*(counter3-1)+counter15*(counter5-1)+a)
