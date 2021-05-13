N = int(input())
H = list(map(int, input().split()))
f = 0
maxtmp = H[0]
shave = 0
for i in range(N-1):
  if H[i]-1>H[i+1] or (H[i]-1==H[i+1] and shave==1):
    f = 1
    break
  elif H[i]-1==H[i+1] and shave==0:
    maxtmp = H[i+1]
    shave = 1
  elif H[i]==H[i+1]:
    pass
  else:
    maxtmp = H[i+1]
    shave = 0
if f == 0:
  print("Yes")
else:
  print("No")