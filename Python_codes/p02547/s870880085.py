N=int(input())
zoro=0

for n in range(N):
  D1,D2=map(int,input().split())
  if D1==D2:
    zoro+=1
  else:
    zoro=0
  
  if zoro==3:
    print("Yes")
    exit()
    
print("No")