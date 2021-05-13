n = int(input())
s = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = alphabet.upper()
alphabets = [w for w in alphabet]

words = []
for i in s:
    index = alphabets.index(i)
    new_index = index + n
    if new_index > 25:
        new_index -= 26
    words.append(alphabets[new_index])

ans = ''.join(words)
print(ans)