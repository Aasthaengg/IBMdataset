S = list(input())

if S[len(S)-1] != 's':
  S.append('s')
else:
  S.append('es')

print(''.join(S))
