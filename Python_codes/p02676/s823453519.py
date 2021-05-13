n = input()
n = int(n)
word = input()
if n >= len(word):
    print(word)
else:
    for i in range(n):
        print(word[i], end='')
    print('...')
