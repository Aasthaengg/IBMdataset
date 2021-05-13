H,N=map(int,input().split())
A=list(map(int,input().split()))
a=sorted(A,reverse=True)
for i in a:
  H-=i
  if H<=0:
    print("Yes")
    exit()
print("No")
