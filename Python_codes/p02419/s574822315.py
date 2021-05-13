w = str(input()).lower()

c = 0
while True:
  L = list(str(input()).split())
  if L[0] == 'END_OF_TEXT':
    break
  for word in L:
    if word.lower() == w:
      c += 1
  
print (c)
