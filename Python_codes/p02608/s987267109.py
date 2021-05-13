n=int(input())
l=[0]*(n+1)
for i in range(1,10**2+1):
  for j in range(1,10**2+1):
    for k in range(1,10**2+1):
      tmp=i*i+j*j+k*k+i*j+j*k+k*i
      if tmp<=n:
        l[tmp]+=1
for li in l[1:]:
  print(li)
