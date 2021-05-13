n=int(input())
a=list(map(int,input().split()))
a.sort()
s=0
for i in range(n):
  if n%2==0:
    if i%2==0:
      s+=a[i]
  else:
    if i%2!=0:
      s+=a[i]

print(sum(a)-s*2)