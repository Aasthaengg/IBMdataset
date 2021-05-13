A,B,C=map(int,input().split())
#t=100//A
#if 100%A==0:
#  t+=1
#d=[A*(i+1) for i in range(t)]
#M=sum(d)
j=0
while j<=10000000:
  if j%B==C:
    print("YES")
    break
  j+=A
else:
  print("NO")