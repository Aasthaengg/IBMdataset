S = input()

cnt = 0
i = 1

while i < len(S):
  if S[i] == S[i-1]:
    cnt += 1
    i += 2
  i += 1

print(len(S)-cnt)