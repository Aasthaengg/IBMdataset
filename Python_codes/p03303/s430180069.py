import re
S = input()
w = int(input())
v = [S[i: i+w] for i in range(0, len(S), w)]
result = ""
for text in v:
    text = list(text)
    result += text[0]
print(result)