S = input()
minimum = 100000000000

for i in range(len(S)-2):

  if minimum > abs(753 - int(S[i:i+3])):
    minimum = abs(753 - int(S[i:i+3]))
    
print(minimum)