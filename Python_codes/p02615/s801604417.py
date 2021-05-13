N = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

count = 0
if N % 2 == 0:
  for i in range(int(N/2)):
    count += 2 * a[i]
  count -= a[0]
else:
  for i in range(int((N+1)/2)):
    count += 2 * a[i]
  count -= a[0]
  count -= a[int((N-1)/2)]
    
print(count)