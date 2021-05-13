N = int(input())
data = list(map(int, input().split()))
Alice = 0
Bob = 0
count = 0
while N > count:
  high = data[0]
  point = 0
  for i in range(N):
    if data[i] > high:
      high = data[i]
      point = i
  if count % 2 == 0:
    Alice += high
  else:
    Bob += high
  data[point] = 0
  count += 1
print(Alice - Bob)