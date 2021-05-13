N=int(input())
L=list(map(int,input().split()))
T=True
for i in L:
  if not(i%3==0 or i%5==0) and i%2==0:
    T=False
if T==True:
  print("APPROVED")
else:
  print("DENIED")