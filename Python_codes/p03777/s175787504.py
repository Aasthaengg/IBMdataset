a, b = input().split()

result = ''
if(a == 'H' and b == 'H'):
  result = 'H'
elif(a == 'H' and b == 'D'):
  result = 'D'
elif(a == 'D' and b == 'H'):
  result = 'D'
elif(a == 'D' and b == 'D'):
  result = 'H'

print(result)
