h,n=input().split()
h=int(h)
n=int(n)
#print(h,n)
arr=list(map(int,input("\r").strip().split()))[:n] 
sum=0;
for i in range(0,n):
  #  print(arr[i])
    sum+=arr[i]
  
if sum>=h:
    print("Yes")
else:
    print("No")
    
   