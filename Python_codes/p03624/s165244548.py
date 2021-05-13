s = input()

alphabet = [chr(i) for i in range(97, 97+26)]

for i in range(len(s)):
    if s[i] in alphabet:
        alphabet.remove(s[i])

if alphabet:
    print(alphabet[0])
else:
    print('None')