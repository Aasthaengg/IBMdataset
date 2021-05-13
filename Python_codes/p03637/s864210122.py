n=int(input())
a=list(map(int,input().split()))
c2=0
c4=0
for i in range(n):
  if a[i]%4==0: c4+=1
  elif a[i]%2==0: c2+=1
if c4>=n//2: print("Yes")
elif (n//2-c4)*2<=c2: print("Yes")
else: print("No")
