n = int(input())
a = list(map(int, input().split()))

sum = 0
mx = 0
for i in range(1, n):
  mx = max(a[i-1], mx)
  sum+=max(mx -a[i], 0)
  
print(sum)