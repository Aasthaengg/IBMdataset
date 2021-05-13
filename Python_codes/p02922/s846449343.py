a, b = map(int, input().split())
un = 1
tap_num = 0
while not un >= b:
  un += a-1
  tap_num += 1
print(tap_num)