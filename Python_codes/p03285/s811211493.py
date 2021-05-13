"""
k,s=map(int,input().split())
x=[0]*k
for i in range(0,k):
  x[i]=i
x.append(k)
a=int(s/3)-1
count=0
for i in range(0,len(x)):
  stemp=s-x[i]
  for j in range(0,min(k+1,stemp)):
    if stemp-x[j] in x:
      count=count+1
print(count)
"""
n=int(input())
temp=[]
i=1
j=0
while True:
  temp.append(i*4+j*7)
  i=i+1
  if (i-1)*4+j*7>100:
    i=0
    j=j+1
  if j>=15:
    break
for i in range(0,len(temp)):
  if temp[i]==n:
    print("Yes")
    break
else:
  print("No")
