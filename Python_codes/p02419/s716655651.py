word = input()
count = 0
while 1:
    line = input()
    if line == 'END_OF_TEXT':
        break
    count += line.lower().split().count(word)
print(count)