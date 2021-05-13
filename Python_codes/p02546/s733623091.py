S = input()
if S[len(S)-1] == 's':
    answer = S + 'es'
else:
    answer = S + 's'
print(answer)
