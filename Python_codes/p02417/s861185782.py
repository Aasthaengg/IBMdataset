import sys
alphabet = "abcdefghijklmnopqrstuvwxyz"
dictionary = {}
for character in alphabet:
    dictionary[character] = 0

for line in sys.stdin:
    for character in line.strip():
        if character.lower() in dictionary:
            dictionary[character.lower()] += 1

for character in alphabet:
    print(character + ' : ' + str(dictionary[character]))