n = int(input())
a = [int(k) for k in input().split()]
cnt = 0
for i in range(n-2):
  if a[i] < a[i+1] and a[i+1] < a[i+2]:cnt += 1
  elif a[i] > a[i+1] and a[i+1] > a[i+2]:cnt += 1
print(cnt)
