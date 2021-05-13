n = int(input())
ans = [0]*n
ans2 = [0]*n
a=list(map(int, input().split()))
b=list(map(int, input().split()))
amax=0
bmax=0

for i in range(n//2):
  if a[i]>amax:
    amax=a[i]
    ans[i]=1
    ans2[i]=a[i]
  elif a[i]<amax:
    print(0)
    quit()
  else:
    ans[i]=amax
  if b[-(i+1)]>bmax:
    bmax=b[-(i+1)]
    ans[-(i+1)]=1
    ans2[-(i+1)]=b[-(i+1)]
  elif b[-i-1]<bmax:
    print(0)
    quit()
  else:
    ans[-(i+1)]=bmax

if n%2==1:  
  i=n//2
  if a[i]>amax:
    amax=a[i]
    ans[i]=1
    ans2[i]=a[i]
  elif a[i]<amax:
    print(0)
    quit()
  else:
    ans[i]=amax
    
for i in range(n//2, n):
  if a[i]>amax:
    amax=a[i]
    if ans[i]==1 and a[i]!=ans2[i]:
        print(0)
        quit()
    elif ans[i] != 1 and ans[i]<a[i]:
      print(0)
      quit()
    ans[i]=1
  elif a[i]<amax:
    print(0)
    quit()
  else:
    ans[i]=min(amax, ans[i])
  if b[-(i+1)]>bmax:
    bmax=b[-(i+1)]
    if ans[-(i+1)]==1 and b[-(i+1)]!=ans2[-(i+1)]:
        print(0)
        quit()
    elif ans[-i-1]!=1 and ans[-i-1]<b[-i-1]:
      print(0)
      quit()
    ans[-(i+1)]=1
  elif b[-i-1]<bmax:
    print(0)
    quit()
  else:
    ans[-(i+1)]=min(bmax, ans[-(i+1)])
    
kotae=1
for i in range(n):
  kotae*=ans[i]
  kotae%=(10**9+7)
print(kotae)