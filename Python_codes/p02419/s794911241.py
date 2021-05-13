# Finding a Word
import re

word = input()
text = ""

end = 0
while end == 0:
    input_line = input()
    if input_line == 'END_OF_TEXT':
        end += 1
    else:
        text += input_line
        text += " "

blocked = text.lower().split() # この方法では記号を取り除けないという問題がある
count = 0
for a in blocked:
    if a == word:
        count += 1
print(count)

