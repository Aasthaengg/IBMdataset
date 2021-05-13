text = input()

def checkHitachi(text):
  # odd length
  if (len(text)%2 != 0): 
    return 'No'
  # even length
  for i in range(0, len(text)-1, 2):
    if (text[i:i+2]!='hi'):
      return 'No'

  return 'Yes'
 
print(checkHitachi(text))
