import sys
alphabet = "abcdefghijklmnopqrstuvwxyz"
sentence = sys.stdin.read()

for letter in alphabet:
    print(letter, ":", sentence.lower().count(letter))
