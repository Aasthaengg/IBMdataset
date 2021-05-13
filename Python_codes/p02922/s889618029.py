A, B = map(int, input().split())

count = 0
avail = 1

while avail < B:
  avail -= 1
  count += 1
  avail += A

print(count)
