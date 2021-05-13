n,y=map(int,input().split())

a,b,c=-1,-1,-1

for i in range(n+1):
  for j in range(n+1):
    h=n-i-j
    if 10000*i+5000*j+1000*h==y and h>=0:
      a,b,c=i,j,h
      break

print("{} {} {}".format(a,b,c))