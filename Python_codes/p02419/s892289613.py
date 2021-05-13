word = input().lower()
text = []
while True:
    line = input()
    if line == "END_OF_TEXT":
        break
    text += line.lower().split()
print(len([x for x in text if x == word]))

