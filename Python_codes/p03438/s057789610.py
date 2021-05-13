n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

c=0
ne=0
for i in range(n):
  c+=max((b[i]-a[i])//2,0)
  ne+=max(a[i]-b[i],0)

print("Yes" if c>=ne else "No")