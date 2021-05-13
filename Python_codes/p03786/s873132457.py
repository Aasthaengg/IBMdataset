from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n=int(input())
a=lnii()
a.sort()

b=[0]
for i in range(1,n+1):
  b.append(b[i-1]+a[i-1])
b=b[1:]

ans=1
for i in range(n-2,-1,-1):
  if b[i]*2>=a[i+1]:
    ans+=1
  else:
    break

print(ans)