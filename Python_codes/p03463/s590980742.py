n,a,b =list(map(int,input().split()))
if(abs(a-b-1)%2==0):
  print("Borys")
elif(abs(a-b-1)%2==1):
  print("Alice")
else:
  print("Draw")