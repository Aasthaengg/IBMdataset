N,M=list(map(int,input().split()))
if any([N%3==0,(N+M)%3==0,M%3==0]):
   print("Possible")
else:
   print("Impossible")