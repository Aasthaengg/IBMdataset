h = int(input())

count = 0

while h > 0:
  h //= 2
  count += 1

print( 2 ** count - 1 )
