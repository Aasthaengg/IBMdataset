n = int(input())

for i in range(1,10):
  r = n/i
  if 1 <= r <= 9 and r == int(r):
    print("Yes")
    exit()
    
print("No")