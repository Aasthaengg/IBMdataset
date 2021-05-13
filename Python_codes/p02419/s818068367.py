word = raw_input()
words = []
count = 0
while True:
    in_line = raw_input().split()
    words += in_line
    if words[len(words)-1] == 'END_OF_TEXT':
        break
for w in words:
    if w.lower() == word:
        count += 1
print count