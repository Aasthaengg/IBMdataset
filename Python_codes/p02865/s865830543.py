N=int(input())
if N==1 or N==2:
  ans=0
elif N%2==0:
  ans=(N/2)-1
else:
  ans=N//2  
print(int(ans))