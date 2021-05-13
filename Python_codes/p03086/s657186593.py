S = input()
Answer = 0
for i in range(len(S)):
    counter = 0
    for j in range(len(S)-i):
        if S[j] in ['A','C', 'G','T']:
            counter += 1
            if Answer < counter:
                Answer = counter
            j = i + 1
        else:
            counter = 0
print(Answer)