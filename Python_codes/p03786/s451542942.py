n=int(input())
a=list(sorted(map(int,input().split())))
s=0
t=0
for i in range(n-1):
  s+=a[i]
  if a[i+1]>2*s:
    t=i+1
print(n-t)