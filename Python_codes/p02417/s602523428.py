import sys
word = [chr(i) for i in range(97, 97+26)]
word_number = []
lines = ""
for line in sys.stdin:
    lines += line

for target in word:
    count = 0
    for character in lines:
        if character.lower() == target:
            count += 1
    word_number.append(count)

for i in range(26):
    print("{0} : {1}".format(word[i],word_number[i]))