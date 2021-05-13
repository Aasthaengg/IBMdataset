W = input()
ls = []
count = 0
while True:
    text = input()
    if text == 'END_OF_TEXT':
        break
    else:
        ls.append(list(map(str, text.split())))
for i in ls:
    for s in i:
        if s.lower() == W.lower():
            count += 1
print(count)