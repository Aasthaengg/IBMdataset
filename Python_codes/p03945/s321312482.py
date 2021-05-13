import re

S = input()
S = re.sub('[B]{2,}', 'B', S)
S = re.sub('[W]{2,}', 'W', S)

print(len(S)-1)
