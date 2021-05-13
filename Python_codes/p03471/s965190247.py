n,y=map(int,input().split())
for i in range(y//10000+1):
  num=y-i*10000
  for j in range(num//5000+1):
    if n-i-j>=0 and (n-i-j)*1000==num-j*5000:
      print(i,j,n-i-j)
      exit()
print(-1,-1,-1)