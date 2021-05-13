n,m = map(int,input().split())
a = [ int(input()) for _ in range(m)]
M=10**9+7
lis = [1] + [0]*n

for i in a:
  lis[i]=-1
lis[1] += 1
for i in range(n-1):
  if lis[i+2]<0:
    lis[i+2]= 0
  else:
    lis[i+2] = (lis[i+1] + lis[i])%M
print(lis[n])