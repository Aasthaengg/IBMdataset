s = input()

words = [s[i-1] for i in range(1, len(s)+1, 1) if i%2 != 0]
print(''.join(words))