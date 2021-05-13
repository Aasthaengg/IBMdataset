word = input()

if word[-1] == 's':
  countable = word + 'es'
else:
  countable = word + 's'
  
print(countable)