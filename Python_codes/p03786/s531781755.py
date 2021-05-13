n=int(input())
a=list(map(int,input().split()))
wa=0
a.sort()
count=0
for i in range(n-1):
  if 2*(wa+a[i])>=a[i+1]:
    count+=1
  else:
    count=0
  wa+=a[i]
print(count+1)