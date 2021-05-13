N=int(input())
W=list(map(int,input().split()))
for i in range(N-1,0,-1):
  if W[i-1]>W[i]+1:
    print("No")
    exit()
  elif W[i-1]==W[i]+1:
    W[i-1]-=1
print("Yes")