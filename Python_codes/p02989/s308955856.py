n = int(input())
dl = list(map(int,input().split()))
dl.sort()

if n % 2 != 0:
  print(0)
  exit()

  
left = dl[(n//2)-1]
right = dl[(n//2)]

print(right-left)
