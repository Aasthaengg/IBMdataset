S = input()

answer = 'Good'
for i in range(len(S)-1):
  if S[i] == S[i+1]:
    answer = 'Bad'

print(answer)