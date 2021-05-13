import sys

n=int(input())
h=list(map(int,input().split()))
h=h[::-1]
be=h[0]

for i in range(n):
  if h[i]-be==1:
    be=h[i]-1
    continue
    
  if h[i]>be:
    print("No")
    sys.exit()
  
  be=h[i]
  
print("Yes")