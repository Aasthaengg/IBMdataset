N = int(input())
result = 0

for x in range(N):
  if (x+1)%3 == 0:
    result+=1

print(result)
