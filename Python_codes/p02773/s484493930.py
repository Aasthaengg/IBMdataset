n = int(input())

words = {}
for i in range(n):
  word = input()
  if word in words:
    words[word] += 1
  else :
    words[word] = 1
words_sorted = sorted(words.items(), key=lambda x:x[1], reverse=True)    
score = words_sorted[0][1]
answers = []
for word in words_sorted:
  if score == word[1]:
    answers.append(word[0])
  else :
    break
    
for answer in sorted(answers) :
  print(answer)