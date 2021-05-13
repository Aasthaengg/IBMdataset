h,w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

hw = [['0' for i in range(w)] for j in range(h) ]

index = 0
for i in range(h):
  for j in range(w):
    if i % 2 == 0:
      hw[i][j] = str(index+1)
        
    else:
      hw[i][w-j-1] = str(index+1)
      
    a[index] -= 1
    if a[index] == 0:
      index += 1
        
for i in range(h):
  print(' '.join(hw[i]))