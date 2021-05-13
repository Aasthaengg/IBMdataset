N = int(input())

for _ in range(N):
  a = int(input())
  if a % 2 == 1:
    print('first')
    exit()
  
print('second')