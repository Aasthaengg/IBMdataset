a, b, k = map(int, input().split())

com_dev = [1]

for i in range(2, 101):
  
    if a % i == 0 and b % i == 0:
        com_dev.append(i)

print(com_dev[len(com_dev) - k])