n = int(input())
arr = {}
for i in range(n):
  a,b= map(int, input().split( ))
  if b in arr:
    arr[b] += a
  else:
    arr[b] = a
time = 0
arrs = sorted(arr.items(), key=lambda x:x[0])
for lin in arrs:
  time += lin[1]
  if lin[0] < time:
    print('No')
    exit()
print('Yes')  