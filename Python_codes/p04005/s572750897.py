a=list(map(int,input().split()))

for i in range(3):
  if a[i]%2==0:
    print(0)
    exit()

a.sort()
ma=a[0]*a[1]
print(ma*(a[2]//2+1)-ma*(a[2]//2))