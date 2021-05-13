N,D=map(int,input().split())
total=0
i=0
while N>total:
  i+=1
  total=(2*D+1)*i
print(i)