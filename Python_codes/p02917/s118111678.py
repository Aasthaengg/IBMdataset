n=int(input())
a=list(map(int,input().split()))
total=a[0]+a[-1]
for i in range(n-2):
  total+=min(a[i],a[i+1])
print(total)