N = int(input())
numbers = list(map(int, input().split()))

P = round(sum(numbers)/N)

sum = 0
for i in range(N):
  sum += (numbers[i] - P)**2

print(sum)