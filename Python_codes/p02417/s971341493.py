word = []
counter = [0]*26
alphabed = list('abcdefghijklmnopqrstuvwxyz')
try:
  while True:
    input_word = list(input().lower())
    if word == '':
      break
    for i in range(len(input_word)):
      word.append(input_word[i])
except EOFError:
  pass
for i in range(len(word)):
  for j in range(26):
    if word[i] == alphabed[j]:
      counter[j] += 1
for i in range(26):
  print('%s : %d'%(alphabed[i], counter[i]))
