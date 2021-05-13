x = int(input())
time = 0
 
for i in range(1,10**10):
  time += i
  if time >= x:
    print(i)
    exit()