n = int(input())

for i in range(n):
  if (i+10) % 3 == 0 or '3' in str(i+1):
    print( " ", i+1, sep = '', end = '' )

print("")