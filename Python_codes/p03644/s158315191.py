N = int(input())

pivot = 0

while True:
  if 2 ** (pivot+1) <= N:
    pivot += 1
  else:
    break 

print(2 ** pivot)