n = int(input())

arr = list(map(int, input().split()))

arr2 = sorted(arr)

count = 0 

for i in range(0,n):
  if arr[i] != arr2[i]: count += 1
if count <= 2: print("YES")
else: print("NO")
