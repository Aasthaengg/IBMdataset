n = int(input())
counter = 0

for i in range(1, n+1):
  counter += 1 if len(str(i))%2==1 else 0

print(counter)
