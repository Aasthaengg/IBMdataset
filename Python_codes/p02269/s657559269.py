n = int(input())
dictionary = {}
for _ in range(n):
    command, word = input().split()
    if command == 'insert':
        dictionary[word] = word
    else:
        if dictionary.get(word) != None:
            print('yes')
        else:
            print('no')
