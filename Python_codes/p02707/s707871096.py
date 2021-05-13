n=int(input())
hoge=[0  for i in range(n)]
huga=list(map(int,input().split()))
for i in range(n-1):
  hoge[huga[i]-1]+=1
  
for i in range(n):
  print(hoge[i])