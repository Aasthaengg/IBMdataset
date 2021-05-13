a,b=map(int,input().split())
for i in (a,b,a+b):
  if i%3==0:
    print("Possible")
    exit()
    
print("Impossible")
