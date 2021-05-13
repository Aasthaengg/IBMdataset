import copy
n=int(input())
a=list(map(int,input().split()))
a.sort()
c=i=st=0

while i <n-1:
  
  if 2*(a[st]+c) >= a[i+1]:
    c+=a[i+1]
    i+=1
    
  else:
    c=a[st]+c
    st=i+1
    i+=1
    
print(n-st)