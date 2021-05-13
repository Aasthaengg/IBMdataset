import re
pattern = str(input())
words = []
while True:
    line = str(input())
    if line == 'END_OF_TEXT':
        break
    words += line.split()

cnt = 0
for word in words:
    if re.fullmatch(pattern, word.lower()):
        cnt += 1
print(cnt)

