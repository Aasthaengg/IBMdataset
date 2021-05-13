n = int(input())

mins = []
maxs = []

for i in range(n):
  a, b = map(int, input().split())
  mins.append(a)
  maxs.append(b)
  
mins.sort()
maxs.sort()

if n % 2 == 1:
  mid = n // 2
  print(maxs[mid] - mins[mid] + 1)
else:
  mid1 = n//2
  mid2 = mid1 - 1
  smallest = mins[mid1] + mins[mid2]
  largest = maxs[mid1] + maxs[mid2]
  print(largest - smallest + 1)