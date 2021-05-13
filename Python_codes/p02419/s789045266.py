word = input().lower()
number = 0
while True:
    line = input()
    if line == 'END_OF_TEXT':
        break
    line = line.replace('.', ' ').replace("'", " ").replace('"', ' ').replace('?',' ').replace('!', ' ').replace(',',' ')
    wordlist = list(line.lower().split())
    number += wordlist.count(word)
print(number)