W = input().lower()
words = ''
while True:
    word = input()
    if word == 'END_OF_TEXT':
        break
             
    words = words + word.lower() + " "
print(sum([1 for c in words.split() if c == W]))

