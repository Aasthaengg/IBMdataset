n = int(input())
a = list(map(int,input().split()))
count = 0
for i in range(1,n-1):
  if min(a[i-1],a[i+1]) < a[i] and max(a[i-1],a[i+1]) > a[i]:
    count += 1
    
print(count)