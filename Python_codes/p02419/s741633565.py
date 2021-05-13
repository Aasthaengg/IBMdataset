word = input()
word_list = []
while True:
    line = input()
    if line == 'END_OF_TEXT':
        break
    line = (line.lower()).split()
    word_list.extend(line)
print(word_list.count(word))