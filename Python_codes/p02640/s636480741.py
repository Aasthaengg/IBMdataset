x, y = list(map(int,input().split()))

for i in range(x+1):
  n = x - i
  s = 2 * n + 4 * i
  if s == y:
    print("Yes")
    exit()
  
print("No")