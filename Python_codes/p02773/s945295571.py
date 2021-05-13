N = int(input())
words = {}
for _ in range(N):
  word = input()
  if word in words:
    words[word] += 1
  else:
    words[word] = 1
sorted_words = sorted(words.items(), key=lambda x: (-x[1], x[0]))
max_v = sorted_words[0][1]
for k, v in sorted_words:
  if v == max_v:
    print(k)
  else:
    exit()
  
