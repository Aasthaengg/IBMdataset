n = int(input())
hp = list(map(int, input().split()))
sum = 0

for i in range(n):
  for j in range(n):
    if i != j:
      sum += (hp[i]*hp[j])

sum = int(sum/2)
print(sum)


  
