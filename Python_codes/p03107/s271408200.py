S = list(input())

i = 0
count = 0
while i < len(S)-1:
  if S[i] != S[i+1]:
    del S[i:i+2]
    count += 2
    if i != 0:
      i -= 1
  else:
    i += 1
print(count)