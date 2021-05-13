N = int(input())
cur = 1

for i in range(1, 10):  
  if cur > N:
    print(cur//2)
    exit()
  cur *= 2
