n=int(input())
a,b=map(str,input().split())

for i,j in zip(a,b):
  print(i+j,end='')