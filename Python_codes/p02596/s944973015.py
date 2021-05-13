n = int(input()) 
curr = 0
for i in range(1,1000000):
  curr = curr * 10 + 7
  curr = curr % n

  if curr == 0:
    print(i)
    exit()
print(-1)