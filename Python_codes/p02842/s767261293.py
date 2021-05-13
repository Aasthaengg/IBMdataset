n = int(input())

for i in range(n+1):
  if int(i*1.08+0.00001)==n:
    print(i)
    exit()
print(":(")