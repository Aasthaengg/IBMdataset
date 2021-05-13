N,A,B=map(int,input().split())
if A>B:
  print(0)
  exit()
elif N==1:
  if A!=B:
    print(0)
    exit()
print((N-2)*(B-A)+1)
  
