word = list(input())

rep_word = []
num_abb = len(word) - 2

rep_word.append(word[0])
rep_word.append(str(num_abb))
rep_word.append(word[-1])

print(''.join(rep_word))