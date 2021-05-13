n,k=map(int,input().split())
a=list(map(int,input().split()))
for i in range(k-1,n-1):
  if int(a[i-k+1]) < int(a[i+1]):
    print("Yes")
    i+=1
  elif int(a[i-k+1])>=int(a[i+1]):
    print("No")
    i+=1
