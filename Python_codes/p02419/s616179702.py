word = input().lower()
texts = []
while True:
  str = input()
  if str == 'END_OF_TEXT':
    break
  texts.extend([s.lower() for s in str.split()] )
    

ans = texts.count(word)

print(ans)