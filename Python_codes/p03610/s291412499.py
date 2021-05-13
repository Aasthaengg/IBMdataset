word = input()
test = [n for i, n in enumerate(word) if i % 2 == 0]
print(''.join(test))