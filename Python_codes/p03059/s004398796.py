a, b , t = map(int, input().split())

time = a
count = 0
while time <= t + 0.5:
  count += b
  time += a
print(count)