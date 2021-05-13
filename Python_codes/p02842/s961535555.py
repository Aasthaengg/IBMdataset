n = int(input())

for i in range(1,n+1):
  x = i * 108
  x //= 100
  if x == n:
    print(i)
    exit()
print(":(")